import requests


class User:
    """
    This class offers method to let you create a new user.
    """

    def __init__(self):
        super().__init__()

    def create_user(self, app_token):
        """Create a new user in your application

        :param app_token: application token
        :type app_token: string
        :return: user object
        :rtype: object
        """
        token = "Bearer" + app_token
        url = "https://api.datavillage.me/users/"
        payload = {}
        headers = {
            "Content-Type": "application/json",
            "Authorization": token,
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def get_user(self, user_id, app_token):
        """Get user details

        :param user_id: [description]
        :type user_id: [type]
        """
        token = "Bearer" + app_token
        url = "https://api.datavillage.me/users/" + user_id
        payload = {}
        headers = {
            "Content-Type": "application/json",
            "Authorization": token,
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text.encode("utf8")

    def get_user_token(self, user, app_token):
        """get user access token based on the applicaiton token

        :param user: unique user identifier
        :type user: string
        :param app_token: application token
        :type app_token: string 
        :return: [description]
        :rtype: [type]
        """

        token = "Bearer" + app_token
        url = "https://api.datavillage.me/users/" + user + "/token"
        payload = {}
        headers = {"Content-Type": "application/json", "Authorization": token}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
