"""
Parser for gradle.lock and build.gradle files
Based on
https://docs.gradle.org/current/userguide/dependency_locking.html
https://docs.gradle.org/current/userguide/dependency_management_for_java_projects.html
"""
import re
from pathlib import Path
from textwrap import dedent
from typing import List
from typing import Optional
from typing import Tuple

import semgrep.semgrep_interfaces.semgrep_output_v1 as out
from semdep.external.parsy import any_char
from semdep.external.parsy import regex
from semdep.external.parsy import string
from semdep.external.parsy import success
from semdep.parsers.util import consume_line
from semdep.parsers.util import DependencyFileToParse
from semdep.parsers.util import DependencyParserError
from semdep.parsers.util import mark_line
from semdep.parsers.util import safe_parse_lockfile_and_manifest
from semdep.parsers.util import transitivity
from semgrep.semgrep_interfaces.semgrep_output_v1 import Ecosystem
from semgrep.semgrep_interfaces.semgrep_output_v1 import FoundDependency
from semgrep.semgrep_interfaces.semgrep_output_v1 import Fpath
from semgrep.semgrep_interfaces.semgrep_output_v1 import Maven
from semgrep.semgrep_interfaces.semgrep_output_v1 import ScaParserName
from semgrep.verbose_logging import getLogger

logger = getLogger(__name__)

# Examples:
# ch.qos.logback.contrib:logback-json-classic:0.1.5=productionRuntimeClasspath,runtimeClasspath,testRuntimeClasspath
dep = mark_line(regex("([^:]+:[^:]+):([^=]+)=[^\n]+", flags=0, group=(1, 2)))

# Parser for comments
comment_line = regex(r"#.*\n")

# If we hit a line that isn't simple, like this:
#     implementation fileTree(dir: "libs", include: ["*.jar"])
# just ignore it
# Examples:
#   implementation "com.mx.path-core:http"å
manifest_line = (
    regex(
        dedent(
            r"""
    [\sa-zA-Z]+       # whitespace, followed by "implementation" or "testImplementation" or any number of other things
    ["']              # opening quote
        ([^:]+:[^:]+) # package name
        (?::[^']+)?   # optional version
    ["']"""
        ),  # closing quote
        flags=re.VERBOSE,
        group=1,
    )
    | consume_line
)

# Ignore everything before and after the dependencies data
manifest = (
    any_char.until(string("dependencies {\n"), consume_other=True)
    >> (manifest_line | success(None))
    .sep_by(string("\n"), min=1)
    .map(lambda xs: {x for x in xs if x})
    << any_char.many()
)

gradle = (
    comment_line.many()  # Optionally parse comments at the beginning
    >> (dep | (regex("empty=[^\n]*").result(None)))
    .sep_by(string("\n"))
    .map(lambda xs: [x for x in xs if x])
    << string("\n").optional()
)


def parse_gradle(
    lockfile_path: Path, manifest_path: Optional[Path]
) -> Tuple[List[FoundDependency], List[DependencyParserError]]:
    parsed_lockfile, parsed_manifest, errors = safe_parse_lockfile_and_manifest(
        DependencyFileToParse(
            lockfile_path, gradle, ScaParserName(out.PGradleLockfile())
        ),
        DependencyFileToParse(
            manifest_path, manifest, ScaParserName(out.PGradleLockfile())
        )
        # the matcher might match a build.gradle.kts file, which we don't currently
        # support for manifest parsing. In that case just use the lockfile.
        if manifest_path and manifest_path.name == "build.gradle" else None,
    )
    if not parsed_lockfile:
        return [], errors
    output = []
    for line_number, (package, version) in parsed_lockfile:
        output.append(
            FoundDependency(
                package=package,
                version=version,
                ecosystem=Ecosystem(Maven()),
                resolved_url=None,
                allowed_hashes={},
                transitivity=transitivity(parsed_manifest, [package]),
                line_number=line_number,
                lockfile_path=Fpath(str(lockfile_path)),
                manifest_path=Fpath(str(manifest_path)) if manifest_path else None,
            )
        )
    return output, errors
