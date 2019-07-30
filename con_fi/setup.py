from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def setup(config):
    engine = None
    if config.DATABASE_TYPE == "sqlite":
        db_type = "sqlite:///" + config.SQLITE_CONFIG["location"]
        engine = create_engine(db_type, echo=config.DATABASE_ECHO)

    if config.DATABASE_TYPE == "postgres":
        db = "postgres://{username}:{password}@{host}:{port}/{database}"
        db = db.format(**config.POSTGRES_CONFIG)
        engine = create_engine(db, echo=config.DATABASE_ECHO)
    return sessionmaker(bind=engine)
