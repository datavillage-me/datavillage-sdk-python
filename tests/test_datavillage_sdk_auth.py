from datavillage_sdk import auth
import unittest
import requests


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    def test_request_response(self):
        url = "https://api.datavillage.me/oauth/token"
        payload = {}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == 200
