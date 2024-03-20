import time
from sqlalchemy import (Column, String, DateTime,
                        Date, Text, Table, ForeignKey)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, Base, UUID


def document_path(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("docs", hash_, filename)


class Document(APIBase):

    # DOCUMENT_STATUS_CHOICE = (("active", "active"), ("inactive", "inactive"))

    title = Column(String(1500), nullable=True, default="")
    description = Column(Text, nullable=True, default="")
    document_file = Column(String(1500))

    def __str__(self):
        return self.title

    def get_team_users(self):

        return self.get_team_and_assigned_users

    # t = ((1, 'a'),(2, 'b'))
    # dict((y, x) for x, y in t)
    # dict(map(reversed, t))

    @property
    def get_status_choices(self):
        return dict(self.DOCUMENT_STATUS_CHOICES)

    @property
    def get_team_and_assigned_users(self):
        team_users = [team.users for team in self.teams]
        assigned_users = self.shared_to
        users = team_users + assigned_users
        return users

    @property
    def get_assigned_users_not_in_teams(self):

        team_users = [team.users for team in self.teams]
        assigned_users = self.shared_to
        users = set(assigned_users) - set(team_users)

        return users
