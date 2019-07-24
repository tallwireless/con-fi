# All of the enities to be used

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(25))

    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")

    api_key = relationship("API_Key", back_populates="user")

    # Attributes are stored in the JSON column type. The key is attribute
    # name. Every attribute has a op and value associated with it.
    #    SELECT id, username, json_array_elements(info)->>'attribute' as attribute,
    #                         json_array_elements(info)->>'op' as op,
    #                         json_array_elements(info)->>'value'
    #                as value FROM public.users where id=7;
    attributes = Column(JSON, default={})

    enabled = Column(Boolean, default=True)

    def __init__(self, username, password, role=None):
        self.username = username
        self.set_password(password)
        if role is not None:
            self.role_name = role

    def set_password(self, password):
        self.set_attr("Cleartext-Password", ":=", password)

    def get_attr(self, attr):
        for i in self.attributes.data:
            if i["attribute"] == attr:
                return i

        raise Exception("No such attribute")
        return None

    def set_attr(self, attr, op, value):
        data = {}
        for i in self.attributes.data:
            if i["attribute"] == attr:
                data = i
                self.attributes.data.remove(i)
        i["attribute"] = attr
        i["op"] = op
        i["value"] = value
        self.attributes.data.append(data)
        return data


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    vlan = Column(Integer, default=None)

    users = relationship("User", back_populates="role")


# class API_Key(Base):
#    __tablename__ = "api_keys"
#
#    api_key = Column(String(64), primary_key=True)
#    user_id = Column(Integer, ForeignKey("users.id"))
#
#    user = relationship("User", back_populates="api_key")
#
#    expires = Column(DateTime)
#
#
# class MAC_Address(Base):
#    __tablename__ = "mac_addresses"
#
#    mac = Column(String(17), primary_key=True)
#    reason = Column(String(), nullable=True)
#    time = Column(DateTime)
