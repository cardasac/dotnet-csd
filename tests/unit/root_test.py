from http import HTTPStatus

from flask import Flask


def test_request_example(client: Flask):
    response = client.get("/")
    assert b"Index</h1>" in response.data


def test_ideal_blood_pressure(client: Flask):
    response = client.post(
        "/",
        data={
            "systolic": 120,
            "diastolic": 80,
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert b"Ideal" in response.data
