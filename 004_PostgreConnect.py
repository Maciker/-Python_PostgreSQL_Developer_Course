Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyscopg2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pyscopg2
ModuleNotFoundError: No module named 'pyscopg2'
>>> import psycopg2
>>> connection = psycopg2.connect(database="learning", user="postgres", password="postgre", host="localhost")
>>> cursor = connection.cursor()
>>> cursor.execute("SELECT * FROM purchases")
>>> for row in cursor:
	print row
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(row)?
>>> for row in cursor:
	print(row)

	
(1, 4, 1)
(2, 5, 1)
(3, 6, 1)
(5, 3, 5)
(6, 2, 5)
(7, 4, 2)
(8, 2, 4)
(9, 3, 4)
(10, 6, 5)
(11, 6, 5)
>>> 
