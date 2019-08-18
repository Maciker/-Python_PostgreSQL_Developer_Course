from user import User
from database import Database
from twitter_utils import consumer, get_request_token, get_oauth_verifier, get_access_token

Database.initialise(user='postgres', password='postgre', host='localhost', database='learning')

user_screen_name = input("Enter your Twitter name: ")

user = User.load_from_db_by_screen_name(user_screen_name)

if not user:
    # Press "Sign in" on twitter.com
    # Twitter sends them back to e.g. www.ourwebsite.com/auth
    # we don't have that page, so we are going to generate a pin code
    # We get that auth code + request token -> twitter -> token

    request_token = get_request_token()
    oauth_verifier = get_oauth_verifier(request_token)
    # Combine both token and adding the oauth_verifier
    access_token = get_access_token(request_token, oauth_verifier)
    print(access_token)

    user = User(user_screen_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()

# Store the tweets on a variable
tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=Robert de Niro+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])