from sqlalchemy import (Column, String, Text, ForeignKey, DateTime, 
                        Integer, Boolean)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID


class Note(APIBase):

    title = Column(String(250), nullable=True)
    body = Column(Text, nullable=True)
    remarks = Column(Text, nullable=True)
    creator_id = Column(UUID, ForeignKey("staffs.id"),  nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"),  nullable=True)

    created_by = relationship("Staff", back_populates="actions_created",
                              foreign_keys=[creator_id])
   
    updated_by = relationship("Staff", back_populates="actions_updated",
                              foreign_keys=[updator_id])

    
    reminders = relationship("ActionReminder", back_populates="action" )
    
    #assigned staffs
    assigned_staffs = relationship("ActionStaff", back_populates="action")


    #lead
    leads =  relationship("Lead", secondary="leads_actions", back_populates="actions")


    #consultation
    consultation = relationship("Consultation", back_populates="actions")


    #client
    client = relationship("Client", back_populates="actions")

    #matter


    #contacts
    #contacts = relationship("ActionStaff", back_populates="action")


    def __str__(self):
        return self.name


    @property
    def get_status_choices(self):
        return self.status


    @property
    def get_type(self):
        return self.type


    @property
    def get_team_and_assigned_users(self):
        team_users = [team.users for team in self.teams]
        assigned_users = self.assigned_users
        users = team_users + assigned_users
        return users


    @property
    def get_assigned_users_not_in_teams(self):
        team_users =  [team.users for team in self.teams]
        assigned_users = self.assigned_users
        users = set(assigned_users) - set(team_users)   
        return users


