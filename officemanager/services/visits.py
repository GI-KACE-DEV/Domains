from app.domains.officemanager.models import visit_entry, expected_visitor, utils, visitor
from app.crud.base import CRUDBase
from app.domains.officemanager.schemas.visits import  (
    VisitCategoryCreate, VisitCategoryUpdate,
    VisitStatusCreate, VisitStatusUpdate,
    ExpectedVisitorCreate, ExpectedVisitorUpdate,
    VisitEntryCreate, VisitEntryUpdate,
    OfficeAreaCreate, OfficeAreaUpdate,
    VisitorCreate, VisitorUpdate
)

# Office Area
class CRUDOfficeArea(CRUDBase[utils.OfficeArea, OfficeAreaCreate,
                        OfficeAreaUpdate]):
    pass
    
office_area_actions = CRUDOfficeArea(utils.OfficeArea)


# Visit Status
class CRUDVisitStatus(CRUDBase[visit_entry.VisitStatus, VisitStatusCreate,
                        VisitStatusUpdate]):
    pass
    
visit_status_actions = CRUDVisitStatus(visit_entry.VisitStatus)

    
# Visit Category
class CRUDVisitCategory(CRUDBase[utils.VisitCategory, VisitCategoryCreate, 
                                 VisitCategoryUpdate]):
    pass
    
visit_category_actions = CRUDVisitCategory(utils.VisitCategory)
    

# Expected Visitor
class CRUDExpectedVisitor(CRUDBase[expected_visitor.ExpectedVisitor, ExpectedVisitorCreate, 
                                 ExpectedVisitorUpdate]):
    pass
    
expected_visitor_actions = CRUDExpectedVisitor(expected_visitor.ExpectedVisitor)


# Visit Entry
class CRUDVisitEntry(CRUDBase[visit_entry.VisitEntry, VisitEntryCreate, 
                                 VisitEntryUpdate]):
    pass

visit_entry_actions = CRUDVisitEntry(visit_entry.VisitEntry)

# Visitor
class CRUDVisitor(CRUDBase[visitor.Visitor, VisitorCreate, 
             VisitorUpdate]):
    pass
    
visitor_actions = CRUDVisitor(visitor.Visitor)

