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

    @patch("datavillage_sdk.user.behaviour.requests.post")
    def test_get_behaviour(self, mock_post):
        mock_post.return_value.ok = True
        behaviour = Behaviour()
        response = behaviour.get_behaviour(
            user_id="uesr",
            consent_receipt="consent_receipt_processing",
            behaviour_id="behaviour",
        )
        assert response is not None

    @patch("datavillage_sdk.user.behaviour.requests.post")
    def test_get_all_behaviour(self, mock_post):
        mock_post.return_value.ok = True
        behaviour = Behaviour()
        response = behaviour.get_all_behaviour(
            user_id="uesr", consent_receipt_processing="consent_receipt_processing"
        )
        assert response is not None
