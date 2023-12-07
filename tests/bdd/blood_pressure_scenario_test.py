from pytest_bdd import given, parsers, scenarios, then, when
from src.blood_pressure import calculate_blood_pressure

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
