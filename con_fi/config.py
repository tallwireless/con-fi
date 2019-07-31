import os


##########
#
#  Database Type
#  Possible values are: sqlite, postgres
#
#########
DATABASE_ECHO = os.getenv("DB_DEBUG", False)

#########
#
#  Postgres Settings
#
#########

POSTGRES_CONFIG = {
    "username": os.getenv("POSGRES_USER", "dev"),
    "password": os.getenv("POSGRES_PASSWORD", "dev"),
    "database": os.getenv("POSGRES_DB", "confi"),
    "host": os.getenv("POSTGRES_HOST", "127.0.0.1"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
}

############
#
# Catcha Settings
#
############

# This is the key which is used to encrypt the captcha

# THIS SHOULD BE CHANGED BEFORE DEPLOYMENT

APP_KEY = os.getenv("APP_KEY", "1111111111111111")
