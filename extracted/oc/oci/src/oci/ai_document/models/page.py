# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Page(object):
    """
    One page document analysis result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Page object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param page_number:
            The value to assign to the page_number property of this Page.
        :type page_number: int

        :param dimensions:
            The value to assign to the dimensions property of this Page.
        :type dimensions: oci.ai_document.models.Dimensions

        :param detected_document_types:
            The value to assign to the detected_document_types property of this Page.
        :type detected_document_types: list[oci.ai_document.models.DetectedDocumentType]

        :param detected_languages:
            The value to assign to the detected_languages property of this Page.
        :type detected_languages: list[oci.ai_document.models.DetectedLanguage]

        :param words:
            The value to assign to the words property of this Page.
        :type words: list[oci.ai_document.models.Word]

        :param lines:
            The value to assign to the lines property of this Page.
        :type lines: list[oci.ai_document.models.Line]

        :param tables:
            The value to assign to the tables property of this Page.
        :type tables: list[oci.ai_document.models.Table]

        :param document_fields:
            The value to assign to the document_fields property of this Page.
        :type document_fields: list[oci.ai_document.models.DocumentField]

        :param signatures:
            The value to assign to the signatures property of this Page.
        :type signatures: list[oci.ai_document.models.Signature]

        :param bar_codes:
            The value to assign to the bar_codes property of this Page.
        :type bar_codes: list[oci.ai_document.models.BarCode]

        :param selection_marks:
            The value to assign to the selection_marks property of this Page.
        :type selection_marks: list[oci.ai_document.models.SelectionMark]

        """
        self.swagger_types = {
            'page_number': 'int',
            'dimensions': 'Dimensions',
            'detected_document_types': 'list[DetectedDocumentType]',
            'detected_languages': 'list[DetectedLanguage]',
            'words': 'list[Word]',
            'lines': 'list[Line]',
            'tables': 'list[Table]',
            'document_fields': 'list[DocumentField]',
            'signatures': 'list[Signature]',
            'bar_codes': 'list[BarCode]',
            'selection_marks': 'list[SelectionMark]'
        }
        self.attribute_map = {
            'page_number': 'pageNumber',
            'dimensions': 'dimensions',
            'detected_document_types': 'detectedDocumentTypes',
            'detected_languages': 'detectedLanguages',
            'words': 'words',
            'lines': 'lines',
            'tables': 'tables',
            'document_fields': 'documentFields',
            'signatures': 'signatures',
            'bar_codes': 'barCodes',
            'selection_marks': 'selectionMarks'
        }
        self._page_number = None
        self._dimensions = None
        self._detected_document_types = None
        self._detected_languages = None
        self._words = None
        self._lines = None
        self._tables = None
        self._document_fields = None
        self._signatures = None
        self._bar_codes = None
        self._selection_marks = None

    @property
    def page_number(self):
        """
        **[Required]** Gets the page_number of this Page.
        The document page number.


        :return: The page_number of this Page.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this Page.
        The document page number.


        :param page_number: The page_number of this Page.
        :type: int
        """
        self._page_number = page_number

    @property
    def dimensions(self):
        """
        Gets the dimensions of this Page.

        :return: The dimensions of this Page.
        :rtype: oci.ai_document.models.Dimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this Page.

        :param dimensions: The dimensions of this Page.
        :type: oci.ai_document.models.Dimensions
        """
        self._dimensions = dimensions

    @property
    def detected_document_types(self):
        """
        Gets the detected_document_types of this Page.
        An array of detected document types.


        :return: The detected_document_types of this Page.
        :rtype: list[oci.ai_document.models.DetectedDocumentType]
        """
        return self._detected_document_types

    @detected_document_types.setter
    def detected_document_types(self, detected_document_types):
        """
        Sets the detected_document_types of this Page.
        An array of detected document types.


        :param detected_document_types: The detected_document_types of this Page.
        :type: list[oci.ai_document.models.DetectedDocumentType]
        """
        self._detected_document_types = detected_document_types

    @property
    def detected_languages(self):
        """
        Gets the detected_languages of this Page.
        An array of detected languages.


        :return: The detected_languages of this Page.
        :rtype: list[oci.ai_document.models.DetectedLanguage]
        """
        return self._detected_languages

    @detected_languages.setter
    def detected_languages(self, detected_languages):
        """
        Sets the detected_languages of this Page.
        An array of detected languages.


        :param detected_languages: The detected_languages of this Page.
        :type: list[oci.ai_document.models.DetectedLanguage]
        """
        self._detected_languages = detected_languages

    @property
    def words(self):
        """
        Gets the words of this Page.
        The words detected on the page.


        :return: The words of this Page.
        :rtype: list[oci.ai_document.models.Word]
        """
        return self._words

    @words.setter
    def words(self, words):
        """
        Sets the words of this Page.
        The words detected on the page.


        :param words: The words of this Page.
        :type: list[oci.ai_document.models.Word]
        """
        self._words = words

    @property
    def lines(self):
        """
        Gets the lines of this Page.
        The lines of text detected on the page.


        :return: The lines of this Page.
        :rtype: list[oci.ai_document.models.Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this Page.
        The lines of text detected on the page.


        :param lines: The lines of this Page.
        :type: list[oci.ai_document.models.Line]
        """
        self._lines = lines

    @property
    def tables(self):
        """
        Gets the tables of this Page.
        The tables detected on the page.


        :return: The tables of this Page.
        :rtype: list[oci.ai_document.models.Table]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """
        Sets the tables of this Page.
        The tables detected on the page.


        :param tables: The tables of this Page.
        :type: list[oci.ai_document.models.Table]
        """
        self._tables = tables

    @property
    def document_fields(self):
        """
        Gets the document_fields of this Page.
        The form fields detected on the page.


        :return: The document_fields of this Page.
        :rtype: list[oci.ai_document.models.DocumentField]
        """
        return self._document_fields

    @document_fields.setter
    def document_fields(self, document_fields):
        """
        Sets the document_fields of this Page.
        The form fields detected on the page.


        :param document_fields: The document_fields of this Page.
        :type: list[oci.ai_document.models.DocumentField]
        """
        self._document_fields = document_fields

    @property
    def signatures(self):
        """
        Gets the signatures of this Page.
        The signatures detected on the page.


        :return: The signatures of this Page.
        :rtype: list[oci.ai_document.models.Signature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this Page.
        The signatures detected on the page.


        :param signatures: The signatures of this Page.
        :type: list[oci.ai_document.models.Signature]
        """
        self._signatures = signatures

    @property
    def bar_codes(self):
        """
        Gets the bar_codes of this Page.
        The bar codes detected on the page.


        :return: The bar_codes of this Page.
        :rtype: list[oci.ai_document.models.BarCode]
        """
        return self._bar_codes

    @bar_codes.setter
    def bar_codes(self, bar_codes):
        """
        Sets the bar_codes of this Page.
        The bar codes detected on the page.


        :param bar_codes: The bar_codes of this Page.
        :type: list[oci.ai_document.models.BarCode]
        """
        self._bar_codes = bar_codes

    @property
    def selection_marks(self):
        """
        Gets the selection_marks of this Page.
        The checkboxes and selection marks detected on the page.


        :return: The selection_marks of this Page.
        :rtype: list[oci.ai_document.models.SelectionMark]
        """
        return self._selection_marks

    @selection_marks.setter
    def selection_marks(self, selection_marks):
        """
        Sets the selection_marks of this Page.
        The checkboxes and selection marks detected on the page.


        :param selection_marks: The selection_marks of this Page.
        :type: list[oci.ai_document.models.SelectionMark]
        """
        self._selection_marks = selection_marks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
