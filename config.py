##########
#
#  Database Type
#  Possible values are: sqlite, postgres
#
#########
DATABASE_TYPE = "postgres"

DATABASE_ECHO = True

#########
#
#  SQLite Settings
#
#########

SQLITE_CONFIG = {
    # Location of the SQLite Database
    "location": "env/db.sqlite"
}

POSTGRES_CONFIG = {
    "username": "dev",
    "password": "dev",
    "database": "confi",
    "host": "127.0.0.1",
    "port": "5432",
}
