from sqlalchemy import (Column, String, Date, DateTime,
                        ForeignKey, Table, Text)
from sqlalchemy.orm import relationship

from app.db.base_class import UUID, APIBase, Base


task_staffs = Table(
    'task_staffs', Base.metadata,
    Column('task_id', UUID, ForeignKey('tasks.id')),
    Column('staff_id', UUID, ForeignKey('staffs.id')),
)

# task_teams = Table(
#    'task_teams', Base.metadata,
#    Column('task_id', UUID, ForeignKey('tasks.id')),
#    Column('team_id', UUID, ForeignKey('teams.id')),
# )

'''task_contacts = Table(
    'task_contacts', Base.metadata,
    Column('task_id', UUID, ForeignKey('tasks.id'), primary_key=True),
    Column('contact_id', UUID, ForeignKey('contacts.id'),primary_key=True),
)
'''


class Task(APIBase):

    STATUS_CHOICES = (
        ("New", "New"),
        ("Assigned", "Assigned"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )

    PRIORITY_CHOICES = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))

    title = Column(String(200))
    description = Column(Text)
    status = Column(String(200))
    priority = Column(String(50))
    due_date = Column(Date, nullable=True)

    # client_account_id = Column(UUID, ForeignKey("client_account.id"))

    staff_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    # contacts = relationship("Contact",secondary=task_contacts,
    #                        back_populates="assigned_crm_tasks")

    assigned_to = relationship("Staff", secondary=task_staffs,
                               back_populates="assigned_crm_tasks")
    # teams =  relationship("Team",secondary=task_teams,
    #                      back_populates="assigned_crm_tasks")

    staffs = relationship("Staff", secondary="staffs_tasks",
                          back_populates="assigned_crm_tasks")

    def __str__(self):
        return self.title

    @property
    def get_team_staffs(self):
        team_staffs = [team.staff for team in self.teams]

    @property
    def get_team_and_assigned_users(self):
        team_staffs = self.get_team_staffs()
        assigned_staffs = self.assigned_to
        staffs = team_staffs + assigned_staffs
        return staffs

    # accounts = relationship("Account",secondary="accounts_tasks", back_populates="tasks")
