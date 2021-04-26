import os

import config


class BaseService:

    def app_authentication(self):
        return (f'OAuth oauth_consumer_key="{config.clients["test_client"]["consumer_key"]}", '
                f'oauth_signature_method="PLAINTEXT", '
                f'oauth_signature="{config.clients["test_client"]["consumer_secret"]}&"')

    def member_authentication(self):
        return (f'OAuth oauth_consumer_key="{config.clients["test_client"]["consumer_key"]}", '
                f'oauth_token="{config.clients["test_client"]["oauth_token"]}", oauth_signature_method="PLAINTEXT", '
                f'oauth_signature="{config.clients["test_client"]["consumer_secret"]}&'
                f'{config.clients["test_client"]["oauth_token_secret"]}"')
