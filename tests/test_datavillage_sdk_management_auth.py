from datavillage_sdk.management.auth import Authentication
import unittest
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    @patch("datavillage_sdk.management.auth.requests.post")
    def test_request_response(self, mock_post):
        mock_post.return_value.ok = True
        auth = Authentication()
        response = auth.get_application_token("test", "test")
        assert response is not None
