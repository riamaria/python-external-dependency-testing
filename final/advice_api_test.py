import json

import pytest
import requests_mock

import advice_api
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

        api_client = advice_api.ApiClient(url=GET_ADVICE_URL)

        advice_slip = api_client.get_advice()

        assert isinstance(advice_slip, advice_api.AdviceSlip)
        assert 100 == advice_slip.id
        assert ADVICE == advice_slip.advice


def test_get_advice_500_exception():
    with requests_mock.mock() as mock_client:
        mock_client.register_uri(
            "GET", GET_ADVICE_URL, status_code=500)

        try:
            api_client = advice_api.ApiClient(url=GET_ADVICE_URL)
            api_client.get_advice()
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
def test_get_advice_invalid_response_exception(invalid_response: str):
    with requests_mock.mock() as mock_client:
        mock_client.register_uri(
            "GET", GET_ADVICE_URL, status_code=200, text=json.dumps(invalid_response))

        try:
            api_client = advice_api.ApiClient(url=GET_ADVICE_URL)
            api_client.get_advice()
        except Exception as e:
            expected_error = f"Unexpected JSON response format. Response: {json.dumps(invalid_response)}"
            assert expected_error == str(e)
