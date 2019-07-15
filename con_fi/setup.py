from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def setup(config):
    engine = None
    if config.DATABASE_TYPE == "sqlite":
        db_type = "sqlite:///" + config.SQLITE_CONFIG["location"]
        engine = create_engine(db_type, echo=config.DATABASE_ECHO)

    return sessionmaker(bind=engine)
