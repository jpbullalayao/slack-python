from slack.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA


class Group(CreateableAPIResource):
    OBJECT_NAME = "groups"

    @classmethod
    def post_url(cls):
        return cls.class_url() + 'create'
