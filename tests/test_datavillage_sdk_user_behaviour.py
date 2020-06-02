from datavillage_sdk.user.behaviour import Behaviour
import unittest
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    @patch("datavillage_sdk.user.behaviour.requests.post")
    def test_create_behaviour(self, mock_post):
        mock_post.return_value.ok = True
        behaviour = Behaviour()
        response = behaviour.create_behaviour(
            user="uesr",
            consent_receipt_processing="consent_receipt_processing",
            behaviour="behaviour",
            user_access_token="token",
        )
        assert response is not None
