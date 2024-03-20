from sqlalchemy import (

    Column,  Date, DateTime, ForeignKey, Text, String
)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID


# Create a model for Teams
class Team(APIBase):
    name = Column(String, unique=True)

    # staff
    members = relationship("Staff", secondary="team_staffs",
                           back_populates="teams")

    # actions
    assigned_actions = relationship("Action", secondary="action_teams",
                                    back_populates="assigned_teams")

    # lead

    # client

    # oppotunity

    # brief

    # litigation


class TeamStaff(APIBase):

    team_id = Column(UUID, ForeignKey("teams.id"), primary_key=True)
    staff_id = Column(UUID, ForeignKey("staffs.id"), primary_key=True)
    role = Column(String)

    # team = relationship("Team", back_populates="members",
    #                    secondary="team_staffs")

    # staff = relationship("Staff", back_populates="teams",
    #                     secondary="team_staffs")


# Create a model for Team Users
class TeamUser(APIBase):
    __tablename__ = "team_users"
    team_id = Column(UUID, ForeignKey("teams.id"), primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id"), primary_key=True)
    role = Column(String)
