from sqlalchemy import (Column, String, ForeignKey,)
from app.domains.common.models.utils import CASE_TYPE, PRIORITY_CHOICE, STATUS_CHOICE
from  app.domains.common.models.action import Action
from app.domains.hr.staff.models  import Team


class SupportCase(models.Model):
    name = Column(String(250))
    description = Column())
    status = Column(choices=STATUS_CHOICE, max_length=64)
    priority = models.CharField(choices=PRIORITY_CHOICE, max_length=64)
    case_type = models.CharField(
        choices=CASE_TYPE, max_length=255, blank=True, null=True, default=""
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="accounts_cases",
    )

    contacts = models.ManyToManyField(Contact)
    closed_on = models.DateField()
    assigned_to = models.ManyToManyField(Profile, related_name="case_assigned_users")
    created_by = models.ForeignKey(
        Profile, related_name="case_created_by", on_delete=models.SET_NULL, null=True
    )

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    teams = models.ManyToManyField(Teams, related_name="cases_teams")
    
    org = models.ForeignKey(
        Org, on_delete=models.SET_NULL, null=True, blank=True, related_name="case_org"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    @property
    def get_team_users(self):
        team_user_ids = list(self.teams.values_list("users__id", flat=True))
        return Profile.objects.filter(id__in=team_user_ids)

    @property
    def get_team_and_assigned_users(self):
        team_user_ids = list(self.teams.values_list("users__id", flat=True))
        assigned_user_ids = list(self.assigned_to.values_list("id", flat=True))
        user_ids = team_user_ids + assigned_user_ids
        return Profile.objects.filter(id__in=user_ids)

    @property
    def get_assigned_users_not_in_teams(self):
        team_user_ids = list(self.teams.values_list("users__id", flat=True))
        assigned_user_ids = list(self.assigned_to.values_list("id", flat=True))
        user_ids = set(assigned_user_ids) - set(team_user_ids)
        return Profile.objects.filter(id__in=list(user_ids))

    def get_meetings(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type,
            object_id=self.id,
            event_type="Meeting",
            status="Planned",
        )

    def get_completed_meetings(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Meeting"
        ).exclude(status="Planned")

    def get_tasks(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type,
            object_id=self.id,
            event_type="Task",
            status="Planned",
        )

    def get_completed_tasks(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Task"
        ).exclude(status="Planned")

    def get_calls(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type,
            object_id=self.id,
            event_type="Call",
            status="Planned",
        )

    def get_completed_calls(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Call"
        ).exclude(status="Planned")

    def get_assigned_user(self):
        return Profile.objects.get(id=self.assigned_to_id)

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()



