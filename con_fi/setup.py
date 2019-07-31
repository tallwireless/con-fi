from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from con_fi import config

from con_fi import entities

from flask import Flask


app = Flask("ConFi")


def setup():
    db = "postgres://{username}:{password}@{host}:{port}/{database}"
    db = db.format(**config.POSTGRES_CONFIG)
    config.engine = create_engine(db, echo=config.DB_DEBUG)
    config.SessionMaker = sessionmaker(bind=config.engine)
    initial_setup()


# Create the tables
def initial_setup():
    try:
        app.logger.info("Initial Setup of database...")
        entities.Base.metadata.create_all(config.engine)

        init_role = entities.Role(name=config.DEFAULT_ROLE)

        session = config.SessionMaker()
        session.add(init_role)
        session.commit()
        app.logger.info("Clean Database has been setup")
    except Exception:
        app.logger.info("Database already exists")
