DEBUG = False

######################
#  Database Part #####
######################
DB_USER = '{{ DB_USER }}'
DB_PASSWORD = '{{ DB_PASSWORD }}'
DB_HOST = '{{ DB_HOST }}'
DB_PORT = 5432
DB_DBNAME = '{{ DB_DBNAME }}'
SQLALCHEMY_DATABASE_URI = 'postgresql://{{ DB_HOST }}/{{ DB_DBNAME }}'

DB_POOL_SIZE = 10
DB_MAX_OVERFLOW = 40
