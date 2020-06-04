import json

import jsonschema
import requests

import advice_api


def get_advice():
    api_client = advice_api.ApiClient(url="https://api.adviceslip.com/advice")
    advice_slip = api_client.get_advice()

    return f"Your advice: {advice_slip.advice}"


if __name__ == "__main__":
    print(get_advice())
