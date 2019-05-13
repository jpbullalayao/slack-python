from slack.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA


class Channel(CreateableAPIResource):
    OBJECT_NAME = "channels"
    
    @classmethod
    def post_url(cls):
        return cls.class_url() + 'create'
