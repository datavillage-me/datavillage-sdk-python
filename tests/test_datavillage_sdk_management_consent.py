from datavillage_sdk.management.consent import Consent
import unittest
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    """Test case for the client methods."""

    @patch("datavillage_sdk.management.consent.requests.post")
    def test_create_consent_receipt(self, mock_post):
        mock_post.return_value.ok = True
        consent = Consent()
        response = consent.create_consent_receipt(
            app_token="token",
            name="test",
            description="test",
            purpose="to test",
            duration="1 day",
            data_categories="data_categories",
            data_sources="data sources",
            creator_name="create",
            creator_uri="uri",
            creator_logo="/path",
            behaviour_extracted_frequency="everyday",
        )
        assert response is not None

    @patch("datavillage_sdk.management.consent.requests.get")
    def test_get_consent_receipt(self, mock_get):
        mock_get.return_value.ok = True
        consent = Consent()
        response = consent.get_consent_receipt(
            app_token="token", consent_receipt_processing="test",
        )
        assert response is not None

    @patch("datavillage_sdk.management.consent.requests.get")
    def test_list_consent_receipts(self, mock_get):
        mock_get.return_value.ok = True
        consent = Consent()
        response = consent.list_consent_receipts(app_token="token")
        assert response is not None

    @patch("datavillage_sdk.management.consent.requests.get")
    def test_get_consent(self, mock_get):
        mock_get.return_value.ok = True
        consent = Consent()
        response = consent.get_consent(
            user_access_token="token", consent_receipt_processing="test"
        )
        assert response is not None

    @patch("datavillage_sdk.management.consent.requests.get")
    def test_get_consent_history(self, mock_get):
        mock_get.return_value.ok = True
        consent = Consent()
        response = consent.get_consent_history(user_access_token="token", userid="test")
        assert response is not None
