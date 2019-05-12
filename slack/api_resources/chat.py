from slack.api_resources.abstract.createable_api_resource import CreateableAPIResource

class Chat(CreateableAPIResource):
	OBJECT_NAME = "chat"

	@classmethod
	def post_url(cls):
		return cls.class_url() + 'postMessage'

	


