import os


def get_password():
    if os.getenv('testpassword'):
        return os.getenv('testpassword')
    raise AttributeError('No password was set for the test role. Add environment variable testpassword')


def get_username():
    if os.getenv('testuser'):
        return os.getenv('testuser')
    raise AttributeError('No username was set for the test role. Add environment variable username')


def get_token():
    if os.getenv('token'):
        return os.getenv('token')
    raise AttributeError('No oauthToken was set for client. Add environment variable token')


def get_token_secret():
    if os.getenv('tokensecret'):
        return os.getenv('tokensecret')
    raise AttributeError('No oauthTokenSecret was set for the client. Add environment variable tokensecret')


def get_key():
    if os.getenv('key'):
        return os.getenv('key')
    raise AttributeError('No consumerKey was set for the client. Add environment variable key')


def get_key_secret():
    if os.getenv('keysecret'):
        return os.getenv('keysecret')
    raise AttributeError('No consumerSecret was set for the client. Add environment variable keysecret')


site_urls = {
    'ui': 'https://www.tmsandbox.co.nz',
    'api': 'https://api.tmsandbox.co.nz/v1',
}

clients = {
    'test_client': {
        'oauth_token': get_token(),
        'oauth_token_secret': get_token_secret(),
        'consumer_key': get_key(),
        'consumer_secret': get_key_secret()
    }
}

roles = {
    'test_role': {
        'username': get_username(),
        'password': get_password()
    }
}

selenium_wait_time = 20
