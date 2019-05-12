import requests
import slack


class APIRequestor(object):
    def __init__(
        self,
        key=None,
        client=None,
        api_base=None,
    ):
        self.api_key = key
        self.api_base = api_base or slack.api_base

    def request(self, method, url, params=None, headers=None):
        return self.request_raw(
            method, url, params, headers
        )

    def request_raw(self, method, url, params=None, headers=None):
        if self.api_key:
            my_api_key = self.api_key
        else:
            my_api_key = slack.api_key

        if my_api_key is None:
            # TODO: Raise AuthenticationError here
            return

        abs_url = "{api_base}{url}".format(
            api_base=self.api_base,
            url=url
        )

        request_data = params
        request_data['token'] = my_api_key

        return requests.post(abs_url, data=params)
