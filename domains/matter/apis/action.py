from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


#action_staff
action_staffs = Table(
    'action_staffs', Base.metadata,
    Column('staff_id', UUID, ForeignKey('staffs.id')),
    Column('action_id', UUID, ForeignKey('actions.id'))
)

class Action(APIBase):

    title = Column(String)
    description = Column(Text, nullable=False)
    notes = Column(Text, nullable=True)
    action_type = Column(String)  #meeting , call, email
    date = Column(DateTime)
    status = Column(String)


    assigned_to = relationship("Staff", secondary="action_staffs", 
                            back_populates="actions_assigned")

    assigned_by = relationship("Staff", foreign_keys="Action.assigned_by_id",
                                back_populates="actions_assigned_by")


    #matter
    matters = relationship("Matter", back_populates="actions",
                          secondary="matters_actions")
    
    
    #case
    

    #trial

    
    #lead


    #client_registration


    #consultation

    

    def __str__(self):
        return self 
 