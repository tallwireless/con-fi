import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from con_fi import entities

engine = None

# Set up the Engine
if config.DATABASE_TYPE == "sqlite":
    db = "sqlite:///" + config.SQLITE_CONFIG["location"]
    engine = create_engine(db, echo=config.DATABASE_ECHO)

if config.DATABASE_TYPE == "postgres":
    db = "postgres://{username}:{password}@{host}:{port}/{database}"
    db = db.format(**config.POSTGRES_CONFIG)
    print(db)
    engine = create_engine(db, echo=config.DATABASE_ECHO)

# Create the tables
try:
    entities.Base.metadata.create_all(engine)

    init_role = entities.Role(name="default")

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(init_role)
    session.commit()
except Exception:
    print("Database already exists")
