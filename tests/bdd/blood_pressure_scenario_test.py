import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from src.blood_pressure import calculate_blood_pressure


# Happy path tests with various realistic test values
@pytest.mark.parametrize(
    "systolic, diastolic, expected",
    [
        (115, 75, "Ideal"),
        (125, 85, "Pre-High"),
        (145, 95, "High"),
        (85, 65, "Low"),
    ],
)
def test_calculate_blood_pressure_happy_path(systolic, diastolic, expected):
    # Act
    result = calculate_blood_pressure(systolic, diastolic)

    # Assert
    assert result == expected


# Edge cases
@pytest.mark.parametrize(
    "systolic, diastolic, expected",
    [
        (70, 40, "Low"),
        (190, 100, "High"),
        (120, 80, "Ideal"),
        (125, 80, "Pre-High"),
        (140, 90, "High"),
    ],
)
def test_calculate_blood_pressure_edge_cases(systolic, diastolic, expected):
    # Act
    result = calculate_blood_pressure(systolic, diastolic)

    # Assert
    assert result == expected


# Error cases
@pytest.mark.parametrize(
    "systolic, diastolic, error",
    [
        (None, 80, TypeError),
        (120, None, TypeError),
        ("120", 80, TypeError),
        (120, "80", TypeError),
        (69, 80, ValueError),
        (120, 39, ValueError),
        (191, 80, ValueError),
        (120, 101, ValueError),
    ],
)
def test_calculate_blood_pressure_error_cases(
    systolic,
    diastolic,
    error,
):
    with pytest.raises(error):
        calculate_blood_pressure(systolic, diastolic)


scenarios("features/blood_pressure.feature")


@given(
    parsers.parse("I have bp values of {systolic:d} and {diastolic:d}"),
    target_fixture="bp_values",
)
def bp_values(systolic, diastolic):
    """I have bp values of 120 and 80."""
    return {"systolic": systolic, "diastolic": diastolic}


@when("I calculate the blood pressure", target_fixture="some_thing")
def get_actual_blood_pressure(bp_values):
    """I calculate the blood pressure."""
    return calculate_blood_pressure(
        bp_values["systolic"],
        bp_values["diastolic"],
    )


@then(parsers.parse("I should get {bp:l} blood pressure"))
def some_other(some_thing, bp):
    assert some_thing == bp
