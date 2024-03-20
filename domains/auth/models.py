from sqlalchemy import(
     event, Boolean, Column, ForeignKey, Integer, 
     String, DateTime,  Table
)
from sqlalchemy.orm import relationship
#from passlib.hash import pbkdf2_sha256 as sha256
from datetime import datetime , timedelta
from app.db.base_class import APIBase
from app.db.base_class import Base
#from pydantic import UUID4
from typing import List 
from app.db.base_class import UUID
import datetime
#from app.domains.hr.staff.models  import                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        import Staff


user_roles = Table(
    "user_roles", Base.metadata,
        Column("user_id",UUID, ForeignKey("users.id" ) ),
        Column("role_id",UUID, ForeignKey("roles.id" ))
    )


user_permissions = Table(
    "user_permissions", Base.metadata,
    Column("user_id",UUID, ForeignKey("users.id" )),
    Column("permission_id", UUID, ForeignKey("permissions.id" ) )

    )

role_permissions  = Table(
    "role_permissions", Base.metadata,
    Column("role_id",UUID, ForeignKey("roles.id")),
    Column("permission_id",UUID, ForeignKey("permissions.id"))

    )


class Role(APIBase):
    title= Column(String, nullable=False, unique=True)
    desription = Column(String, nullable=True)
    default = Column(Boolean, nullable=False, default=False)

    #permissions
    permissions = relationship("Permission",  secondary="role_permissions", back_populates="roles")

    #user
    users = relationship("User", secondary="user_roles", back_populates="roles")
 

    def __str__(self):
        return self.title

    
class Permission(APIBase):
    title= Column(String, nullable=False, unique=True)
    desription = Column(String, nullable=True)

    def __str__(self):
        return self.title

    users = relationship("User", secondary="user_permissions", back_populates="permissions")
    roles = relationship("Role",secondary="role_permissions",  back_populates="permissions")


class User(APIBase):

    email = Column(String(150), unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String, nullable=True)
    cellphone = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True)
    staff_id = Column(UUID, ForeignKey("staffs.id"),  nullable=True)


    def __str__(self):
        return f"{self.email}" 


    def create_access_token(self, ):
        pass       

    def decode_access_token(self, token):
        pass
 

    def add_permission(self, permission_id ):
        pass


    def delete_permissions(self, permission_ids: List):
        pass


    def add_roles(self, role_ids: List[UUID]):
        pass


    def delete_roles(self, permission_id: UUID):
        pass
  
    #staff
    #staff = relationship("Staff",  uselist=False, back_populates="user")

    #role 
    roles = relationship("Role", secondary="user_roles", back_populates="users")

    #permissions
    permissions = relationship("Permission", secondary="user_permissions", back_populates="users")


class RevokedToken(APIBase):
    jti = Column(String)
    

class ResetPasswordToken(APIBase):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(UUID, ForeignKey("users.id") , unique=True)
    token = Column(String, index=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)


