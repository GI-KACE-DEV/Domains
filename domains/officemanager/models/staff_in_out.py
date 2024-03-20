from typing import List
from sqlalchemy import (Column, String, Text,Boolean,Integer, Date,Table, ForeignKey )
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from app.db.base_class import Base
from app.domains.common.models.document import Document
