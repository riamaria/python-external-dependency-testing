import json

import jsonschema
import requests

# This is used to validate the API response
get_advice_schema = {
    "type": "object",
    "additionalProperties": False,
    "required": ["slip"],
    "properties": {
        "slip": {
            "type": "object",
            "additionalProperties": False,
            "required": ["id", "advice"],
            "properties": {
                "id": {"type": "integer"},
                "advice": {"type": "string"}
            }
        }
    }
}


def get_advice():
    # TODO replace with api client

    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code != 200:
        raise Exception("Error trying to load API")

    response_body = response.json()
    try:
        jsonschema.validate(instance=response_body, schema=get_advice_schema)
    except jsonschema.exceptions.ValidationError:
        raise Exception(
            f"Unexpected JSON response format. Response: {response.text}")

    # Print out advice
    advice = response_body["slip"]["advice"]

    return f"Your advice: {advice}"


if __name__ == "__main__":
    print(get_advice())
