import mysql.connector

def open_connection():
  config = {
    'user': 'root',
    'password': 'strongpassword',
    'host': '127.0.0.1',
    'database': 'testdb',
    'raise_on_warnings': True
  }

  return mysql.connector.connect(**config)


def close_connection(cnx):
  cnx.close()