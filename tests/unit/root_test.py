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
        follow_redirects=True,
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.history) == 1
    assert response.request.path == "/result"
    assert b"Ideal" in response.data


def test_negative_submit_form(client: Flask):
    response = client.post(
        "/",
        data={
            "systolic": 200,
            "diastolic": 80,
        },
        follow_redirects=True,
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.history) == 0
    assert response.request.path == "/"


def test_get_result(client: Flask):
    response = client.get("/result?result=Ideal&systolic=120&diastolic=80")
    assert response.status_code == HTTPStatus.OK
    assert b"Ideal" in response.data


def test_get_form(client: Flask):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert b"Index" in response.data
