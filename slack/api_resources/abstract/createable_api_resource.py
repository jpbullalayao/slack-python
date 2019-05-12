from slack.api_resources.abstract.api_resource import APIResource
from slack.api_requestor import APIRequestor

class CreateableAPIResource(APIResource):
    @classmethod
    def create(
        cls,
        api_key=None,
        **params
    ):
        requestor = APIRequestor(
            api_key
        )
        url = cls.post_url()
        response = requestor.request("post", url, params)
        # response, api_key = requestor.request("post", url, params, headers)
        # return util.convert_to_slack_object(
        # 	response, api_key
        # )
