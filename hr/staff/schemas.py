from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
from uuid import UUID, UUID
from pydantic import EmailStr

from datetime import datetime, date

from pydantic import EmailStr


'''
from datetime import datetime
from uuid import UUID, UUID
from pydantic import BaseModel, Field

class Model(BaseModel):
    uid: UUID = Field(default_factory=UUID)
    updated: datetime = Field(default_factory=datetime.utcnow)

    Optional[x] is simply short hand for Union[x, None]

'''


class HTTPError(BaseModel):
    detail: str


class RelatedObject(BaseModel):
    ids: List[UUID]

# Shared properties


class DepartmentBase(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    # department_head_id: Optional[UUID] = None


# Properties to receive via API on creation
class DepartmentCreate(DepartmentBase):
    name: str
    location: Optional[str] = None
    # department_head_id: Optional[UUID] = None


# Properties to receive via API on update
class DepartmentUpdate(DepartmentBase):
    name: Optional[str] = None
    location: Optional[str] = None


class DepartmentInDBBase(DepartmentBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DepartmentSchema(DepartmentInDBBase):
    pass


# Additional properties stored in DB
class DepartmentInDB(DepartmentInDBBase):
    pass


# Designation
# Shared properties
class DesignationBase(BaseModel):
    title: Optional[str] = None
    min_salary: Optional[float] = 0.0
    maximum_salary: Optional[float] = 0.0
    rate_per_case: Optional[float] = 0.0
    rate_per_hour: Optional[float] = 0.0
    commission_per_case: Optional[float] = 0.0


# Properties to receive via API on creation
class DesignationCreate(DesignationBase):
    title: str


# Properties to receive via API on update
class DesignationUpdate(DesignationBase):
    title: Optional[str] = None
    description: Optional[str] = None


class DesignationInDBBase(DesignationBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DesignationSchema(DesignationInDBBase):
    pass


# Additional properties stored in DB
class DesignationInDB(DesignationInDBBase):
    pass


# sector
# Shared properties
class SectorBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive via API on creation
class SectorCreate(SectorBase):
    title: str
    description: Optional[str] = None


# Properties to receive via API on update
class SectorUpdate(SectorBase):
    title: Optional[str] = None
    description: Optional[str] = None


class SectorInDBBase(SectorBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SectorSchema(SectorInDBBase):
    pass


# Additional properties stored in DB
class SectorInDB(SectorInDBBase):
    pass


# Practice Area
# Shared properties
class PracticeAreaBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive via API on creation
class PracticeAreaCreate(PracticeAreaBase):
    title: str


# Properties to receive via API on update
class PracticeAreaUpdate(PracticeAreaBase):
    title: Optional[str] = None
    description: Optional[str] = None


class PracticeAreaInDBBase(PracticeAreaBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class PracticeAreaSchema(PracticeAreaInDBBase):
    pass


# Additional properties stored in DB
class PracticeAreaInDB(PracticeAreaInDBBase):
    pass


# Qualification
# Shared properties
class QualificationBase(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None


# Properties to receive via API on creation
class QualificationCreate(QualificationBase):
    title: str
    description: Optional[str] = None


# Properties to receive via API on update
class QualificationUpdate(QualificationBase):
    title: Optional[str] = None
    description: Optional[str] = None


class QualificationInDBBase(QualificationBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class QualificationSchema(QualificationInDBBase):
    pass


# Additional properties stored in DB
class QualificationInDB(QualificationInDBBase):
    pass


# Shared properties
class StaffBase(BaseModel):

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    tin: Optional[str] = None
    ssn: Optional[str] = None
    national_id: Optional[str] = None
    nhis: Optional[str] = None

    official_email: Optional[str] = None
    personal_email: Optional[str] = None
    cellphone_1: Optional[str] = None
    cellphone_2: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    registration_number: Optional[str] = None
    year_called_to_bar: Optional[date] = None

    department_id: Optional[UUID] = None
    designation_id: Optional[UUID] = None
    # supervisor_id: Optional[UUID] = None
    leave_days: Optional[int] = 0
    sick_days: Optional[int] = 0
    overtime_allowed: Optional[bool] = False
    hire_date: Optional[date] = None
    end_date: Optional[date] = None
    salary: Optional[float] = None

    rate_per_matter: Optional[float] = None
    # rate_per_hour: Optional[float] = None
    commission_per_matter: Optional[float] = None
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True

# Properties to receive via API on creation


class StaffCreate(StaffBase):
    personal_email: EmailStr
    first_name: str
    last_name: str
    personal_email: str
    cellphone_1: str
    practice_area_ids: Optional[List[UUID]] = []
    sector_ids: Optional[List[UUID]] = []


# Properties to receive via API on creation
class StaffCreateWithoutRelated (StaffBase):
    personal_email: EmailStr
    first_name: str
    last_name: str
    personal_email: str
    cellphone_1: str
    # practice_area_ids: Optional[List[UUID]] = []
    # sector_ids: Optional[List[UUID]] = []


# Properties to receive via API on update
class StaffUpdate(StaffBase):
    pass


class StaffInDBBase(StaffBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class StaffSchema(StaffInDBBase):

    designation: Optional[DesignationSchema] = None
    department: Optional[DepartmentSchema] = None
    sectors: Optional[List[SectorSchema]]
    practice_areas: Optional[List[PracticeAreaSchema]]


# Additional properties stored in DB
class StaffInDB(StaffInDBBase):
    pass


# Team
class TeamBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


# Properties to receive via API on creation
class TeamCreate(TeamBase):
    name: str
    description: Optional[str]
    # staffs: List[StaffSchema] = []


# Properties to receive via API on update
class TeamUpdate(TeamBase):
    pass


class TeamInDBBase(TeamBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class TeamSchema(TeamInDBBase):
    Team: str
    description: int
    staffs: List[StaffSchema] = []


# Additional properties stored in DB
class TeamInDB(TeamInDBBase):
    pass
