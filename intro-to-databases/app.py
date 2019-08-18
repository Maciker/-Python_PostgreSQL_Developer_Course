from database import Database
# Importamos clase User
from user import User


Database.initialise(user='postgres', password='postgre', database='learning', host='localhost')

# Creamos el primer usuario
#my_user = User('ikermacaya@gmail.com', 'Iker', 'Macaya', None)
# Escribir usuario en la DB
# my_user.save_to_db()
# new users
#erku = User('erku.erku@gmail.com', 'Erkuden', 'Ayala', None)
#erku.save_to_db()
#print(erku)
#asier = User('asiermacaya@gmail.com', 'Asier', 'Macaya', None)
#asier.save_to_db()
#print(asier)
# Cargar usuario de la DB
my_user = User.load_from_db_by_email('asiermacaya@gmail.com')

# my_user.save_to_db()

#print(my_user.email)
# Imprimimos con el metodo repr
print(my_user)