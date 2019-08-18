from database import CursorFromConnectionPool

# Creamos la clase User
class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

# Metodo para imprimir el objeto
    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        #with psycopg2.connect(user='postgres', password='postgre', database='learning', host='localhost') as connection:
        # request connection from the pool
        #with connection_pool.getconn() as connection: == connection = connection_pool.getconn() and nothing more
        #connection = connection_pool.getconn()
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                            (self.email, self.first_name, self.last_name))
        #connection_pool.putconn(connection)
        #connection.commit()
        #connection.close()
        # al usar el with al crear la conexion el commit y el close nos lo hace automaticamente. No con el connection_pool

    @classmethod
    def load_from_db_by_email(cls, email):
        #with psycopg2.connect(user='postgres', password='postgre', database='learning', host='localhost') as connection:
        #with connection_pool.getconn() as connection:
        #connection = connection_pool.getconn()
        with CursorFromConnectionPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email=%s',(email,))
            user_data = cursor.fetchone()
            return cls(user_data[1], user_data[2], user_data[3], user_data[0])