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
    "systolic, diastolic, error, error_message",
    [
        (None, 80, TypeError, "Systolic or diastolic is not an integer"),
        (120, None, TypeError, "Systolic or diastolic is not an integer"),
        ("120", 80, TypeError, "Systolic or diastolic is not an integer"),
        (120, "80", TypeError, "Systolic or diastolic is not an integer"),
        (69, 80, ValueError, "Systolic or diastolic is too low"),
        (120, 39, ValueError, "Systolic or diastolic is too low"),
        (191, 80, ValueError, "Systolic or diastolic is too high"),
        (120, 101, ValueError, "Systolic or diastolic is too high"),
    ],
)
def test_calculate_blood_pressure_error_cases(
    systolic,
    diastolic,
    error,
    error_message,
):
    with pytest.raises(error) as exc_info:
        calculate_blood_pressure(systolic, diastolic)
    assert str(exc_info.value) == error_message
