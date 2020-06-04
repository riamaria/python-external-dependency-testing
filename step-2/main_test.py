import json

import pytest
import requests_mock

import main

GET_ADVICE_URL = "https://api.adviceslip.com/advice"
ADVICE = "Elegance is the only beauty that never fades."


def test_get_advice_successful():
    sample_advice = {
        "slip": {
            "id": 100,
            "advice": ADVICE
        }
    }

    with requests_mock.mock() as mock_client:
        mock_client.register_uri(
            "GET", GET_ADVICE_URL, status_code=200, text=json.dumps(sample_advice))

        advice = main.get_advice()

        expected_message = "Your advice: Elegance is the only beauty that never fades."
        assert expected_message == advice


def test_get_advice_500_exception():
    with requests_mock.mock() as mock_client:
        mock_client.register_uri(
            "GET", GET_ADVICE_URL, status_code=500)

        try:
            main.get_advice()
        except Exception as e:
            assert "Error trying to load API" == str(e)


invalid_responses = [
    [],
    {},
    {"slip": {}},
    {"slip": {"id": 100}},
    {"slap": {"id": 100, "advice": ADVICE}},
    [{"slip": {"id": 100, "advice": ADVICE}}],
]


@pytest.mark.parametrize("invalid_response", invalid_responses)
def test_get_advice_invalid_response_exception(invalid_response: object):
    response_string = json.dumps(invalid_response)
    with requests_mock.mock() as mock_client:
        mock_client.register_uri(
            "GET", GET_ADVICE_URL, status_code=200, text=response_string)

        try:
            main.get_advice()
        except Exception as e:
            expected_error = f"Unexpected JSON response format. Response: {response_string}"
            assert expected_error == str(e)
