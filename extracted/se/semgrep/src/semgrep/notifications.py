from typing_extensions import Final

from semgrep.constants import Colors
from semgrep.util import with_color
from semgrep.verbose_logging import getLogger

HAS_SHOWN_SETTINGS_KEY: Final = "has_shown_metrics_notification"

logger = getLogger(__name__)


def possibly_notify_user() -> None:
    from semgrep.state import get_state

    state = get_state()
    settings, metrics = state.settings, state.metrics

    has_shown = False
    try:
        has_shown = settings.get(HAS_SHOWN_SETTINGS_KEY, False)
    except PermissionError:
        logger.debug("Semgrep does not have access to user settings file")

    if metrics.is_enabled and not has_shown:
        logger.warning(
            with_color(
                Colors.yellow,
                "METRICS: Using configs from the Registry (like --config=p/ci) reports pseudonymous rule metrics to semgrep.dev."
                """\nTo disable Registry rule metrics, use "--metrics=off"."""
                "\nWhen using configs only from local files (like --config=xyz.yml) metrics are sent only when the user is logged in."
                "\n"
                "\nMore information: https://semgrep.dev/docs/metrics"
                "\n",
            )
        )
        settings.set(HAS_SHOWN_SETTINGS_KEY, True)
