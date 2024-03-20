from sqlalchemy import (Column, String,Text, ForeignKey, DateTime, Date,Table, Numeric)
from sqlalchemy.orm import relationship
from app.db.base import APIBase,  Base, UUID
import datetime


class MatterTask(APIBase):
    
    title = Column(String(7000))
    description = Column(String(5000))
    matter_id = Column(UUID, ForeignKey("matters.id"))
    assigner_id = Column(UUID, ForeignKey("staffs.id"))
    assignee_id = Column(UUID, ForeignKey("staffs.id"))
    expected_start_date = Column(DateTime, nullable=True)
    expected_due_date = Column(DateTime, nullable=True)
    actual_start_date = Column(DateTime, nullable=True)
    actual_end_date = Column(DateTime, nullable=True)
    status = Column(String(10), default="pending") 
    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)
    

    matter = relationship("Matter", back_populates="matter_tasks")
    
    #staff
    assignee = relationship("Staff", back_populates="matter_tasks_assigned_to",
                            foreign_keys="MatterTask.assignee_id")
    
    assigner = relationship("Staff", back_populates="matter_tasks_assigned_by",
                            foreign_keys="MatterTask.assigner_id")


    created_by = relationship("Staff", 
                                back_populates="matter_tasks_created", 
                                foreign_keys="MatterTask.creator_id"
                            )
    
    updated_by = relationship("Staff", 
                                back_populates="matter_tasks_updated",
                                  foreign_keys="MatterTask.updator_id")
    
    
    def __str__(self):
        return f"{self.title}"
    