import os


##########
#
#  Database Type
#  Possible values are: sqlite, postgres
#
#########
DB_DEBUG = os.getenv("DB_DEBUG", False)

#########
#
#  Postgres Settings
#
#########

POSTGRES_CONFIG = {
    "username": os.getenv("POSTGRES_USER", "dev"),
    "password": os.getenv("POSTGRES_PASSWORD", "dev"),
    "database": os.getenv("POSTGRES_DB", "confi"),
    "host": os.getenv("POSTGRES_HOST", "db"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
}
print(POSTGRES_CONFIG)
############
#
# Catcha Settings
#
############

# This is the key which is used to encrypt the captcha

# THIS SHOULD BE CHANGED BEFORE DEPLOYMENT

APP_KEY = os.getenv("APP_KEY", "1111111111111111")


DEFAULT_ROLE = os.getenv("DEFAULT_ROLE_NAME", "default")
