import pytest
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
