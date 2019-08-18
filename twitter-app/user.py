from database import CursorFromConnectionPool
import oauth2
from twitter_utils import consumer
import json


# Creamos la clase User
class User:
    def __init__(self, screen_name, oauth_token, oauth_token_secret, id):
        self.screen_name = screen_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

# Metodo para imprimir el objeto
    def __repr__(self):
        return "<User {}>".format(self.screen_name)

    def save_to_db(self):
        #with psycopg2.connect(user='postgres', password='postgre', database='learning', host='localhost') as connection:
        # request connection from the pool
        #with connection_pool.getconn() as connection: == connection = connection_pool.getconn() and nothing more
        #connection = connection_pool.getconn()
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO users (screen_name, oauth_token, oauth_token_secret) VALUES (%s, %s, %s)',
                            (self.screen_name, self.oauth_token, self.oauth_token_secret))
        #connection_pool.putconn(connection)
        #connection.commit()
        #connection.close()
        # al usar el with al crear la conexion el commit y el close nos lo hace automaticamente. No con el connection_pool

    @classmethod
    def load_from_db_by_screen_name(cls, screen_name):
        #with psycopg2.connect(user='postgres', password='postgre', database='learning', host='localhost') as connection:
        #with connection_pool.getconn() as connection:
        #connection = connection_pool.getconn()
        with CursorFromConnectionPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE screen_name=%s',(screen_name,))
            user_data = cursor.fetchone()
            if user_data:
                return cls(screen_name=user_data[1], oauth_token=user_data[2], oauth_token_secret=user_data[3], id=user_data[0])

    def twitter_request(self, uri, verb='GET'):
        # Create an 'authenticated_token' Token object and use that to perform Twitter API calls on behalf of the user
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        authorized_client = oauth2.Client(consumer, authorized_token)

        # Make Twitter API calls!
        response, content = authorized_client.request(uri, verb)
        if response.status != 200:
            print('An error ocurred when searching')

        return json.loads(content.decode('utf-8'))