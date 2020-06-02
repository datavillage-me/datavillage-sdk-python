from datavillage_sdk.user.cages import Cages
import unittest
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    @patch("datavillage_sdk.user.cages.requests.post")
    def test_query_digital_profile(self, mock_post):
        mock_post.return_value.ok = True
        cage = Cages()
        response = cage.query_digital_profile(query="query", user_access_token="token")
        assert response is not None
