import oauth2
import constants
import urllib.parse as urlparse

# create a consumer, wich uses CONSUMER_KEy and CONSUMER_SECRET to identify our app uniquely
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def get_request_token():
    client = oauth2.Client(consumer)
    # Use the to perform a request for the request token
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print('An error ocurred getting the request token from Twitter!')

    # Get the request token arsing the query string returned
    return dict(urlparse.parse_qsl(content.decode('utf8')))

def get_oauth_verifier(request_token):
    # Ask the user to authorize our app and give us the pin code
    print("Go to the following site in your browser:")
    print(get_oauth_verifier_url(request_token))

    return input("What is the PIN? ")

def get_oauth_verifier_url(request_token):
    return "{}?oauth_token={}".format(constants.AUTHORITAZION_URL, request_token['oauth_token'])


def get_access_token(request_token, oauth_verifier):
    # Create a Token object wich contains the request token, and the verifier
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    # Use the client to get the access token
    # Create a client with our consumer (our app) and the newly created (and verifier) token
    client = oauth2.Client(consumer, token)

    # Ask Twitter for an access token, and Twitter knows it should give us it because we've verified the request token
    response, content = client.request(constants.ACCES_TOKEN_URL, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf8')))