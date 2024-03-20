
#from accounts.models import Account, Tags
#from contacts.models import Contact
#from common.models import Org, Profile
#from common.utils import STAGES, SOURCES, CURRENCY_CODES
#from teams.models import Teams

from app.db.base_class import APIBase

class Opportunity(APIBase):
    
    name = Column(String(250))
    client_account_id = models.ForeignKey(ClientAccount,related_name="opportunities",on_delete=models.CASCADE,
        
    )
    stage = Column(
        #pgettext_lazy("Stage of Opportunity", "Stage"), max_length=64, choices=STAGES
        String(250)
    )
    currency = Column(
        String(250)
        #max_length=3, choices=CURRENCY_CODES, blank=True, null=True
    )
    amount = Column(
        Numeric, nullable = True
        #("Opportunity Amount"), decimal_places=2, max_digits=12, blank=True, null=True
    )
    lead_source = Column(
        #_("Source of Lead"), max_length=255, choices=SOURCES, blank=True, null=True
        String(255), nullable = True
    )
    probability = Column(nullable=True , )
    
    #contacts = models.ManyToManyField(Contact)
    
    
    closed_by = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="oppurtunity_closed_by",
    )
    # closed_on = models.DateTimeField(blank=True, null=True)
    closed_on = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(
        Profile, related_name="opportunity_assigned_to"
    )
    created_by = models.ForeignKey(
        Profile,
        related_name="opportunity_created_by",
        on_delete=models.SET_NULL,
        null=True,
    )
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, blank=True)
    teams = models.ManyToManyField(Teams, related_name="oppurtunity_teams")
    org = models.ForeignKey(
        Org,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="oppurtunity_org",
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()

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
