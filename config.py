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

#########
#
#  Postgres Settings
#
#########

POSTGRES_CONFIG = {
    "username": "dev",
    "password": "dev",
    "database": "confi",
    "host": "127.0.0.1",
    "port": "5432",
}

############
#
# Catcha Settings
#
############

# This is the key which is used to encrypt the captcha

# THIS SHOULD BE CHANGED BEFORE DEPLOYMENT

APP_KEY = "e4669d1e6859d3898bec5a9d"
