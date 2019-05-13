from slack.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA


class Conversation(CreateableAPIResource):
    OBJECT_NAME = "conversations"

    @classmethod
    def post_url(cls):
        return cls.class_url() + 'create'
