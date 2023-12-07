"""Main logic for the server."""
from __future__ import annotations


def calculate_blood_pressure(
    systolic: int | None,
    diastolic: int | None,
) -> str:
    """Calculate blood pressure."""
    systolic_pre_high = 120
    systolic_high = 140
    systolic_min = 70
    systolic_max = 190
    diastolic_pre_high = 80
    diastolic_high = 90
    diastolic_min = 40
    diastolic_max = 100

    if not isinstance(systolic, int) or not isinstance(diastolic, int):
        raise TypeError("Systolic or diastolic is not an integer")

    if systolic < systolic_min or diastolic < diastolic_min:
        raise ValueError("Systolic or diastolic is too low")

    if systolic > systolic_max or diastolic > diastolic_max:
        raise ValueError("Systolic or diastolic is too high")

    if (systolic > systolic_pre_high and systolic < systolic_high) or (
        diastolic > diastolic_pre_high and diastolic < diastolic_high
    ):
        return "Pre-High"
    if (systolic >= systolic_high) or (diastolic >= diastolic_high):
        return "High"

    systolic_low = 90
    diastolic_low = 60

    return (
        "Low"
        if systolic < systolic_low or diastolic < diastolic_low
        else "Ideal"
    )
