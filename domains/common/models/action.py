from sqlalchemy import (Column, String, Text, ForeignKey, DateTime,
                        Integer, Boolean)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID


class ActionStatus(APIBase):
    status = Column(String(25))
    description = Column(Text, nullable=False)

    actions = relationship("Action", back_populates="status")

    def __str__(self):
        return self.status


class ActionType(APIBase):
    type = Column(String, unique=True)
    description = Column(Text, nullable=True)


class ActionContact(APIBase):
    action_id = Column(UUID, ForeignKey("actions.id"))
    contact_id = Column(UUID, ForeignKey("contacts.id"))
    role = Column(String, nullable=True)

    # action
    # action = relationship("Action", back_populates="action_contacts")

    # contactacti
    # contact = relationship("Contact", back_populates="action_contacts")


class ActionTeam(APIBase):

    action_id = Column(UUID, ForeignKey("actions.id"))
    team_id = Column(UUID, ForeignKey("teams.id"))
    role = Column(String, nullable=True)

    # actions = relationship("Action", secondary="action_teams",
    #                       back_populates="assigned_teams")

    # teams = relationship("Team", secondary="action_teams",
    #                     back_populates="assigned_actions")

    # clients
    # clients = relationship("Client", secondary="clients_actions", back_populates="actions")
    # meeting_contacts = relationship("MeetingActionContact", back_populates="action")
    # meeting_staffs  = relationship("MeetingActionStaff", back_populates="action")
    # teams = relationship("ActionTeam", back_populates="action")


class ActionStaff(APIBase):

    action_id = Column(UUID, ForeignKey("actions.id"))
    staff_id = Column(UUID, ForeignKey("staffs.id"))
    role = Column(String, nullable=True)

    # actions = relationship("Action", back_populates="assigned_staffs")
    # assigned_staffs = relationship("Staff", back_populates="assigned_actions")

    # name, start_date, end_date, description, type, status, description,
    # assigned_to, budget, currency,
    # Budget[currency, ,budget, actual_cost, objectitive, impression, expected_cost
    # expected_revenue]


class Action(APIBase):

    title = Column(String(250))
    description = Column(Text, nullable=True)
    action_type_id = Column(UUID, ForeignKey("action_types.id"))
    priority = Column(String(25), nullable=True)  # only for task
    planned_start_date = Column(DateTime, nullable=True)
    planned_end_date = Column(DateTime, nullable=True)
    actual_start_date = Column(DateTime, nullable=True)
    actual_end_date = Column(DateTime, nullable=True)
    status_id = Column(UUID, ForeignKey("action_statuses.id"))
    client_id = Column(UUID, ForeignKey("clients.id"),  nullable=True)
    creator_id = Column(UUID, ForeignKey("staffs.id"),  nullable=True)
    updator_id = Column(UUID, ForeignKey("staffs.id"),  nullable=True)

    # staff
    created_by = relationship("Staff", back_populates="actions_created",
                              foreign_keys=[creator_id])

    updated_by = relationship("Staff", back_populates="actions_updated",
                              foreign_keys=[updator_id])

    # status
    status = relationship("ActionStatus", back_populates="actions")

    # contact
    contacts = relationship("Contact", secondary="action_contacts",
                            back_populates="actions")

    # assigned
    assigned_staffs = relationship("Staff", secondary="action_staffs",
                                   back_populates="assigned_actions")

    assigned_teams = relationship("Team", secondary="action_teams",
                                  back_populates="assigned_actions")
    # lead
    leads = relationship("Lead", secondary="leads_actions",
                         back_populates="actions")

    # clients
    clients = relationship("Client", secondary="clients_actions",
                           back_populates="actions")

    # consultation
    consultations = relationship("Consultation", secondary="consultations_actions",
                                 back_populates="actions")

    # activities
    activities = relationship("ActionActivity", back_populates="action")

    # client

    # brief

    # litigation

    # transaction

    def __str__(self):
        return self.title

    @property
    def team_and_assigned_staffs(self):
        team_staffs = [team.staffs for team in self.assigned_teams]
        assigned_staffs = self.assigned_staffs
        staffs = team_staffs + assigned_staffs
        return staffs

    @property
    def assigned_staff_not_in_teams(self):
        staffs = [staff for staff in self.staff]
        assigned_staffs = self.assigned_staffs
        staffs = set(assigned_staffs) - set(staffs)
        return staffs


class ActionActivity(APIBase):
    action_id = Column(UUID, ForeignKey("actions.id"),  nullable=True)
    staff_id = Column(UUID, ForeignKey("staffs.id"),  nullable=True)
    actual_work_done = Column(Text)
    hours = Column(Integer)

    staff = relationship("Staff", back_populates="action_activities")

    action = relationship("Action", back_populates="activities")
