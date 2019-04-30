from slack.api_resources.abstract.api_resource import APIResource

class CreateableAPIResource(APIResource):
	@classmethod
	def create(
		cls,
		api_key=None
	):
		pass
