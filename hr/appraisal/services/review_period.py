from app.domains.hr.appraisal import models
from app.crud.base import CRUDBase
from app.domains.hr.appraisal import models

from app.domains.hr.appraisal.schemas.review_period import  (
    ReviewPeriodCreate, ReviewPeriodUpdate
)

class CRUDReviewPeriod(CRUDBase[models.ReviewPeriod, ReviewPeriodCreate, ReviewPeriodUpdate]):
    pass
    

review_period_actions = CRUDReviewPeriod(models.ReviewPeriod)

