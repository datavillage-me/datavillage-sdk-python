from datavillage_sdk.management.sources import Sources
import unittest
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    @patch("datavillage_sdk.management.sources.requests.get")
    def test_request_response(self, mock_get):
        mock_get.return_value.ok = True
        sources = Sources()
        response = sources.get_data_sources(app_token="test")
        assert response is not None
