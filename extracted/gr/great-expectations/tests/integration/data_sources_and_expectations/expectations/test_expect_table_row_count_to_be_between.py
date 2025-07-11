import pandas as pd
import pytest

import great_expectations.expectations as gxe
from great_expectations.compatibility import pydantic
from great_expectations.core.result_format import ResultFormat
from great_expectations.datasource.fluent.interfaces import Batch
from tests.integration.conftest import parameterize_batch_for_data_sources
from tests.integration.data_sources_and_expectations.test_canonical_expectations import (
    ALL_DATA_SOURCES,
    JUST_PANDAS_DATA_SOURCES,
)

COL_A = "col_a"
COL_B = "col_b"


DATA = pd.DataFrame({COL_A: [1, 2, None], COL_B: ["a", "b", None]})
EMPTY_DATA = pd.DataFrame({COL_A: [], COL_B: []})


@parameterize_batch_for_data_sources(data_source_configs=ALL_DATA_SOURCES, data=DATA)
def test_golden_path(batch_for_datasource: Batch) -> None:
    expectation = gxe.ExpectTableRowCountToBeBetween(min_value=2, max_value=4)
    result = batch_for_datasource.validate(expectation)
    assert result.success


@pytest.mark.parametrize(
    "expectation",
    [
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=None, max_value=None),
            id="vacuously_true",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=2, max_value=None),
            id="just_min",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=None, max_value=4),
            id="just_max",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=3, max_value=5),
            id="inclusivity",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(
                min_value=None, max_value=None, strict_min=True, strict_max=True
            ),
            id="strict_min_max_vacuously_true",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(
                min_value=2, max_value=None, strict_min=True, strict_max=True
            ),
            id="strict_min_max_just_min",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(
                min_value=None, max_value=4, strict_min=True, strict_max=True
            ),
            id="strict_min_max_just_max",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(
                min_value=2, max_value=4, strict_min=True, strict_max=True
            ),
            id="strict_min_max_inclusive",
        ),
    ],
)
@parameterize_batch_for_data_sources(data_source_configs=JUST_PANDAS_DATA_SOURCES, data=DATA)
def test_success(
    batch_for_datasource: Batch, expectation: gxe.ExpectTableRowCountToBeBetween
) -> None:
    result = batch_for_datasource.validate(expectation)
    assert result.success


@parameterize_batch_for_data_sources(data_source_configs=JUST_PANDAS_DATA_SOURCES, data=EMPTY_DATA)
def test_empty_data(batch_for_datasource: Batch) -> None:
    expectation = gxe.ExpectTableRowCountToBeBetween(min_value=0, max_value=0)
    result = batch_for_datasource.validate(expectation)
    assert result.success


@pytest.mark.parametrize(
    "expectation",
    [
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=8, max_value=None),
            id="just_min",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=None, max_value=1),
            id="just_max",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=4, max_value=4),
            id="bad_range",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=3, max_value=4, strict_min=True),
            id="strict_min_max_observed_same_as_min",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(min_value=2, max_value=3, strict_max=True),
            id="strict_min_max_observed_same_as_max",
        ),
        pytest.param(
            gxe.ExpectTableRowCountToBeBetween(
                min_value=3, max_value=3, strict_min=True, strict_max=True
            ),
            id="strict_min_max_observed_same_as_min_and_max",
        ),
    ],
)
@parameterize_batch_for_data_sources(data_source_configs=JUST_PANDAS_DATA_SOURCES, data=DATA)
def test_failure(
    batch_for_datasource: Batch, expectation: gxe.ExpectTableRowCountToBeBetween
) -> None:
    result = batch_for_datasource.validate(expectation)
    assert not result.success


@pytest.mark.unit
def test_valid_range() -> None:
    with pytest.raises(pydantic.ValidationError):
        gxe.ExpectTableRowCountToBeBetween(min_value=5, max_value=4)


@pytest.mark.unit
def test_valid_runtime_parameters() -> None:
    gxe.ExpectTableRowCountToBeBetween(
        min_value={"$PARAMETER": "param_min_value"},
        max_value={"$PARAMETER": "param_max_values"},
    )


@pytest.mark.unit
def test_invalid_runtime_parameters() -> None:
    with pytest.raises(pydantic.ValidationError):
        gxe.ExpectTableRowCountToBeBetween(
            min_value={"min_value": "param_min_value"},
            max_value={"max_value": "param_max_values"},
        )


@pytest.mark.parametrize(
    "suite_param_value,expected_result",
    [
        pytest.param(True, True, id="success"),
    ],
)
@parameterize_batch_for_data_sources(data_source_configs=JUST_PANDAS_DATA_SOURCES, data=DATA)
def test_success_with_suite_param_strict_min_(
    batch_for_datasource: Batch, suite_param_value: bool, expected_result: bool
) -> None:
    suite_param_key = "test_expect_table_row_count_to_be_between"
    expectation = gxe.ExpectTableRowCountToBeBetween(
        min_value=2,
        max_value=4,
        strict_min={"$PARAMETER": suite_param_key},
        result_format=ResultFormat.SUMMARY,
    )
    result = batch_for_datasource.validate(
        expectation, expectation_parameters={suite_param_key: suite_param_value}
    )
    assert result.success == expected_result


@pytest.mark.parametrize(
    "suite_param_value,expected_result",
    [
        pytest.param(True, True, id="success"),
    ],
)
@parameterize_batch_for_data_sources(data_source_configs=JUST_PANDAS_DATA_SOURCES, data=DATA)
def test_success_with_suite_param_strict_max_(
    batch_for_datasource: Batch, suite_param_value: bool, expected_result: bool
) -> None:
    suite_param_key = "test_expect_table_row_count_to_be_between"
    expectation = gxe.ExpectTableRowCountToBeBetween(
        min_value=2,
        max_value=4,
        strict_max={"$PARAMETER": suite_param_key},
        result_format=ResultFormat.SUMMARY,
    )
    result = batch_for_datasource.validate(
        expectation, expectation_parameters={suite_param_key: suite_param_value}
    )
    assert result.success == expected_result
