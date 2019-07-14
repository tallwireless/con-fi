import config

from sqlalchemy import create_engine

from con_fi import entities

engine = None

# Set up the Engine
if config.DATABASE_TYPE == "sqlite":
    db = "sqlite:///" + config.SQLITE_CONFIG["location"]
    engine = create_engine(db, echo=config.DATABASE_ECHO)

# Create the tables
entities.Base.metadata.create_all(engine)
