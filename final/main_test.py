import json

import pytest
import pytest_mock
import requests_mock

import advice_api
import main


def test_get_advice_successful(mocker):
    mock_advice_slip = advice_api.AdviceSlip(
        100, "Elegance is the only beauty that never fades.")
    mocker.patch.object(advice_api.ApiClient, "get_advice",
                        return_value=mock_advice_slip)

    advice = main.get_advice()

    expected_message = "Your advice: Elegance is the only beauty that never fades."
    assert expected_message == advice


def test_get_advice_exception(mocker):
    mocker.patch.object(advice_api.ApiClient, "get_advice",
                        side_effect=Exception("Something went wrong"))
    try:
        main.get_advice()
    except Exception as e:
        assert "Something went wrong" == str(e)
