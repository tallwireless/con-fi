# All of the enities to be used

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, String, Boolean, Time
from sqlalchemy import ForeignKey


Base = declarative_base()


class NAS(Base):
    __tablename__ = "nas"

    id = Column(Integer, primary_key=True)
    nasname = Column(String, nullable=False, index=True)
    shortname = Column(String, nullable=False)
    type = Column(String, default="other", nullable=False)
    ports = Column(Integer)
    secret = Column(String, nullable=False)
    server = Column(String)
    community = Column(String)
    description = Column(String)


class PostAuth(Base):
    __tablename__ = "radpostauth"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    pass1 = Column(String)
    reply = Column(String)
    CalledStationId = Column(String)
    CallingStationId = Column(String)
    authdate = Column(Time(timezone=True), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(25))

    role_id = Column(Integer, ForeignKey("roles.id"), default=1)

    # Attributes are stored in the JSON column type. The key is attribute
    # name. Every attribute has a op and value associated with it.
    #    SELECT id, username, json_array_elements(info)->>'attribute' as attribute,
    #                         json_array_elements(info)->>'op' as op,
    #                         json_array_elements(info)->>'value'
    #                as value FROM public.users where id=7;
    attr = Column(JSON)

    enabled = Column(Boolean, default=True)

    def __init__(self, username, password, role="default"):
        self.attr = []
        self.username = username
        self.set_password(password)
        if role is not None:
            self.role_name = role

    def set_password(self, password):
        self.set_attr("Cleartext-Password", ":=", password)

    def get_attr(self, attr):
        for i in self.attr.data:
            if i["attribute"] == attr:
                return i

        raise Exception("No such attribute")
        return None

    def set_attr(self, attr, op, value):
        data = {}
        for i in self.attr:
            if i["attribute"] == attr:
                data = i
                self.attr.remove(i)
        data["attribute"] = attr
        data["op"] = op
        data["value"] = value
        self.attr.append(data)
        return data


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(26), unique=True)
    attr = Column(JSON)

    def __init__(self, name, attr=[]):
        self.attr = attr
        self.name = name

    def get_attr(self, attr):
        for i in self.attr.data:
            if i["attribute"] == attr:
                return i

        raise Exception("No such attribute")
        return None

    def set_attr(self, attr, op, value):
        data = {}
        for i in self.attr:
            if i["attribute"] == attr:
                data = i
                self.attr.remove(i)
        data["attribute"] = attr
        data["op"] = op
        data["value"] = value
        self.attr.append(data)
        return data
