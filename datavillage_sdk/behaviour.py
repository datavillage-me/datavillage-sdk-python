import requests


class Behaviour:
    """
    This class offers methods to manage a behaviours

    ``from datavillage_sdk import Behaviour``

    ``behaviour = Behaviour()``

    """

    def __init__(self):
        super().__init__()

    def create_behaviour(
        self, user, consent_receipt_processing, behaviour, user_access_token
    ):
        """Create a new behaviour

        :param user: unique user identifier
        :type user: string
        :param consent_receipt_processing: consent receipt ID 
        :type consent_receipt_processing: string
        :param behaviour: base64 encoded JSON-LD
        :type behaviour: base64
        :param user_access_token: user access token
        :type user_access_token: string
        :return: behaviour instance
        :rtype: object
        """
        token = "Bearer" + user_access_token
        url = (
            "https://api.datavillage.me/behaviors/"
            + user
            + "/"
            + consent_receipt_processing
        )
        payload = behaviour
        headers = {"Content-Type": "application/json", "Authorization": token}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def get_behaviour(self):
        """
        This method is under construction
        """

    def get_all_behaviour(self, user, app_token):
        """
        This method is under construction
        """
