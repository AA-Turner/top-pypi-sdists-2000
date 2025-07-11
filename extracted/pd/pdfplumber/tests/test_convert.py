#!/usr/bin/env python
import json
import logging
import os
import sys
import unittest
from io import StringIO
from subprocess import PIPE, Popen

import pytest

import pdfplumber

logging.disable(logging.ERROR)

HERE = os.path.abspath(os.path.dirname(__file__))


SCOTUS_TEXT = [
    {
        "type": "Div",
        "children": [
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 21.625,
                    "O": "Layout",
                },
                "mcids": [1],
                "text": [
                    "IN THE SUPREME COURT OF THE UNITED STATES - - - - - - - - - - - - "
                    "- - - - - x MICHAEL A. KNOWLES, : WARDEN, :"
                ],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "StartIndent": 86.375,
                    "O": "Layout",
                },
                "mcids": [2],
                "text": [" Petitioner :"],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 50.375,
                    "O": "Layout",
                },
                "mcids": [3, 4],
                "text": [
                    " v. ",
                    ": No. 07-1315 ALEXANDRE MIRZAYANCE. : - - - - - - - - - - - - - -"
                    " - - - x",
                ],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "O": "Layout",
                    "SpaceAfter": 24.5,
                    "LineHeight": 25.75,
                    "StartIndent": 165.625,
                    "EndIndent": 57.625,
                },
                "mcids": [5],
                "text": [" Washington, D.C. Tuesday, January 13, 2009"],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 100.75,
                    "O": "Layout",
                },
                "mcids": [6],
                "text": [
                    " The above-entitled matter came on for oral argument before the "
                    "Supreme Court of the United States at 1:01 p.m. APPEARANCES: "
                    "STEVEN E. MERCER, ESQ., Deputy Attorney General, Los"
                ],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "O": "Layout",
                    "SpaceAfter": 179.125,
                    "LineHeight": 25.75,
                    "TextIndent": 21.625,
                    "EndIndent": 50.375,
                    "TextAlign": "None",
                },
                "mcids": [7],
                "text": [
                    " Angeles, Cal.; on behalf of the Petitioner. CHARLES M. SEVILLA, "
                    "ESQ., San Diego, Cal.; on behalf of the Respondent. "
                ],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {"O": "Layout", "TextAlign": "Center", "SpaceAfter": 8.5},
                "mcids": [8],
                "text": ["1\n"],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {"O": "Layout", "TextAlign": "Center"},
                "mcids": [9],
                "text": ["Alderson Reporting Company "],
            },
        ],
    }
]


def run(cmd):
    return Popen(cmd, stdout=PIPE).communicate()[0]


class Test(unittest.TestCase):
    @classmethod
    def setup_class(self):
        self.path = os.path.join(HERE, "pdfs/pdffill-demo.pdf")
        self.pdf = pdfplumber.open(self.path, pages=[1, 2, 5])

    @classmethod
    def teardown_class(self):
        self.pdf.close()

    def test_json(self):
        c = json.loads(self.pdf.to_json())
        assert (
            c["pages"][0]["rects"][0]["bottom"] == self.pdf.pages[0].rects[0]["bottom"]
        )

    def test_json_attr_filter(self):
        c = json.loads(self.pdf.to_json(include_attrs=["page_number"]))
        assert list(c["pages"][0]["rects"][0].keys()) == ["object_type", "page_number"]

        with pytest.raises(ValueError):
            self.pdf.to_json(include_attrs=["page_number"], exclude_attrs=["bottom"])

        with pytest.raises(ValueError):
            self.pdf.to_json(exclude_attrs=["object_type"])

    def test_json_all_types(self):
        c = json.loads(self.pdf.to_json(object_types=None))
        found_types = c["pages"][0].keys()
        assert "chars" in found_types
        assert "lines" in found_types
        assert "rects" in found_types
        assert "images" in found_types
        assert "curves" in c["pages"][2].keys()

    def test_single_pages(self):
        c = json.loads(self.pdf.pages[0].to_json())
        assert c["rects"][0]["bottom"] == self.pdf.pages[0].rects[0]["bottom"]

    def test_additional_attr_types(self):
        path = os.path.join(HERE, "pdfs/issue-67-example.pdf")
        with pdfplumber.open(path, pages=[1]) as pdf:
            c = json.loads(pdf.to_json())
            assert len(c["pages"][0]["images"])

    def test_csv(self):
        c = self.pdf.to_csv(precision=3)
        assert c.split("\r\n")[9] == (
            "char,1,45.83,58.826,656.82,674.82,117.18,117.18,135.18,12.996,"
            "18.0,12.996,,,,,,,TimesNewRomanPSMT,,,"
            '"(1.0, 0.0, 0.0, 1.0, 45.83, 660.69)"'
            ',,,DeviceRGB,"(0.0, 0.0, 0.0)",,,18.0,,,,"(0,)",,Y,,1,'
        )

        io = StringIO()
        self.pdf.to_csv(io, precision=3)
        io.seek(0)
        c_from_io = io.read()
        assert c == c_from_io

    def test_csv_all_types(self):
        c = self.pdf.to_csv(object_types=None)
        assert c.split("\r\n")[1].split(",")[0] == "line"

    def test_cli_help(self):
        res = run([sys.executable, "-m", "pdfplumber.cli"])
        assert b"usage:" in res

    def test_cli_structure(self):
        res = run([sys.executable, "-m", "pdfplumber.cli", self.path, "--structure"])
        c = json.loads(res)
        # lol no structure
        assert c == []

    def test_cli_structure_text(self):
        path = os.path.join(HERE, "pdfs/scotus-transcript-p1.pdf")
        res = run([sys.executable, "-m", "pdfplumber.cli", path, "--structure-text"])
        c = json.loads(res)
        assert c == SCOTUS_TEXT

    def test_cli_json(self):
        res = run(
            [
                sys.executable,
                "-m",
                "pdfplumber.cli",
                self.path,
                "--format",
                "json",
                "--pages",
                "1-2",
                "5",
                "--indent",
                "2",
            ]
        )

        c = json.loads(res)
        assert c["pages"][0]["page_number"] == 1
        assert c["pages"][1]["page_number"] == 2
        assert c["pages"][2]["page_number"] == 5
        assert c["pages"][0]["rects"][0]["bottom"] == float(
            self.pdf.pages[0].rects[0]["bottom"]
        )

    def test_cli_csv(self):
        res = run(
            [
                sys.executable,
                "-m",
                "pdfplumber.cli",
                self.path,
                "--format",
                "csv",
                "--precision",
                "3",
            ]
        )

        assert res.decode("utf-8").split("\r\n")[9] == (
            "char,1,45.83,58.826,656.82,674.82,117.18,117.18,135.18,12.996,"
            "18.0,12.996,,,,,,,TimesNewRomanPSMT,,,"
            '"(1.0, 0.0, 0.0, 1.0, 45.83, 660.69)"'
            ',,,DeviceRGB,"(0.0, 0.0, 0.0)",,,18.0,,,,"(0,)",,Y,,1,'
        )

    def test_cli_csv_exclude(self):
        res = run(
            [
                sys.executable,
                "-m",
                "pdfplumber.cli",
                self.path,
                "--format",
                "csv",
                "--precision",
                "3",
                "--exclude-attrs",
                "matrix",
                "mcid",
                "ncs",
            ]
        )

        assert res.decode("utf-8").split("\r\n")[9] == (
            "char,1,45.83,58.826,656.82,674.82,117.18,117.18,135.18,12.996,"
            "18.0,12.996,,,,,,,TimesNewRomanPSMT,"
            ',,,"(0.0, 0.0, 0.0)",,,18.0,,,,"(0,)",,Y,,1,'
        )

    def test_cli_csv_include(self):
        res = run(
            [
                sys.executable,
                "-m",
                "pdfplumber.cli",
                self.path,
                "--format",
                "csv",
                "--precision",
                "3",
                "--include-attrs",
                "page_number",
            ]
        )

        assert res.decode("utf-8").split("\r\n")[9] == ("char,1")

    def test_cli_text(self):
        path = os.path.join(HERE, "pdfs/scotus-transcript-p1.pdf")
        res = run(
            [
                sys.executable,
                "-m",
                "pdfplumber.cli",
                path,
                "--format",
                "text",
            ]
        )

        target_path = os.path.join(HERE, "comparisons/scotus-transcript-p1.txt")
        target = open(target_path).read()
        assert res.decode("utf-8") == target

    def test_page_to_dict(self):
        x = self.pdf.pages[0].to_dict(object_types=["char"])
        assert len(x["chars"]) == len(self.pdf.pages[0].chars)
