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


class AdviceSlip():
    """Represents an advice slip"""

    def __init__(self, id: int, advice: str):
        self.id = id
        self.advice = advice


class ApiClient():
    def __init__(self, url: str):
        self.url = url

    def get_advice(self) -> AdviceSlip:
        # Make API request
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Error trying to load API")

        # Make sure that the advice can be retrieved from the response
        response_body = response.json()
        try:
            jsonschema.validate(instance=response_body,
                                schema=get_advice_schema)
        except jsonschema.exceptions.ValidationError:
            raise Exception(
                f"Unexpected JSON response format. Response: {response.text}")

        # Build out the AdviceSlip response
        advice_slip = AdviceSlip(
            response_body["slip"]["id"], response_body["slip"]["advice"])

        return advice_slip
