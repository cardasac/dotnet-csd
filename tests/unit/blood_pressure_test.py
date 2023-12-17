import pytest
from src.blood_pressure import calculate_blood_pressure


@pytest.mark.parametrize(
    "systolic, diastolic, expected",
    [
        (115, 75, "Ideal"),
        (125, 85, "PreHigh"),
        (145, 95, "High"),
        (85, 65, "Ideal"),
        (80, 60, "Ideal"),
        (110, 85, "PreHigh"),
        (130, 95, "High"),
        (80, 50, "Low"),
    ],
)
def test_calculate_blood_pressure_correct_values(
    systolic, diastolic, expected,
):
    result = calculate_blood_pressure(systolic, diastolic)

    assert result == expected


@pytest.mark.parametrize(
    "systolic, diastolic, expected",
    [
        (70, 40, "Low"),
        (190, 100, "High"),
        (120, 80, "Ideal"),
        (125, 80, "PreHigh"),
        (140, 90, "PreHigh"),
    ],
)
def test_calculate_blood_pressure_edge_cases(systolic, diastolic, expected):
    result = calculate_blood_pressure(systolic, diastolic)

    assert result == expected


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
        (120.90, 101, TypeError),
    ],
)
def test_calculate_blood_pressure_error_cases(
    systolic,
    diastolic,
    error,
):
    with pytest.raises(error):
        calculate_blood_pressure(systolic, diastolic)
