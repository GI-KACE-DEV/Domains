
# Create a model for the litigation category
class Category(Base):
    __tablename__ = "categories"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    litigations = relationship("Litigation", back_populates="category")


# Create a model for the litigation tag
class Tag(Base):
    __tablename__ = "tags"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    litigations = relationship("Litigation", secondary="litigation_tags")


# Create a model for the litigation-team association table
litigation_team = Table(
    "litigation_team",
    Base.metadata,
    Column("litigation_id", String, ForeignKey("litigations.id"), primary_key=True),
    Column("user_id", String, ForeignKey("users.id"), primary_key=True)
)


# Create a model for the litigation-tag association table
litigation_tags = Table(
    "litigation_tags",
    Base.metadata,
    Column("litigation_id", String, ForeignKey("litigations.id"), primary_key=True),
    Column("tag_id", String, ForeignKey("tags.id"), primary_key=True)
)


# Create a model for the litigation
class Litigation(Base):
    __tablename__ = "litigations"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    title = Column(String)
    description = Column(String)
    client_id = Column(String, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="litigations")
    category_id = Column(String, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="litigations")
    lawyer_id= Column(String, ForeignKey("users.id"))
    lawyer = relationship("User", backref="litigations")
    staff = relationship("User", secondary=litigation_team)
    documents = relationship("Document", back_populates="litigation")
    tasks = relationship("Task", back_populates="litigation")
    hearings = relationship("Hearing", back_populates="litigation")
    opposing_parties = relationship("OpposingParty", back_populates="litigation")


# Create a model for the client
class Client(Base):
    __tablename__ = "clients"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    email = Column(String)
    litigations = relationship("Litigation", back_populates="client")


# Create a model for the document
class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    title = Column(String)
    file_path = Column(String)
    litigation_id = Column(String, ForeignKey("litigations.id"))
    litigation = relationship("Litigation", back_populates="documents")


# Create a model for the task
class Task(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    description = Column(String)
    assigner_id = Column(String, ForeignKey("users.id"))
    assigner = relationship("User", backref="assigned_tasks")
    assignee_id = Column(String, ForeignKey("users.id"))
    assignee = relationship("User", backref="tasks")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String)
    litigation_id = Column(String, ForeignKey("litigations.id"))
    litigation = relationship("Litigation", back_populates="tasks")


# Create a model for the hearing
class Hearing(Base):
    __tablename__ = "hearings"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    litigation_id = Column(String, ForeignKey("litigations.id"))
    litigation = relationship("Litigation", back_populates="hearings")
    court = Column(String)
    judge = Column(String)
    notes = Column(String)
    comments = relationship("Comment", back_populates="hearing")


# Create a model for the comment
class Comment(Base):
    __tablename__ = "comments"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    text = Column(String)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", backref="comments")
    hearing_id = Column(String, ForeignKey("hearings.id"))
    hearing = relationship("Hearing", backref="comments")


# Create a model for the opposing party
class OpposingParty(Base):
    __tablename__ = "opposing_parties"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    litigation_id = Column(String, ForeignKey("litigations.id"))
    litigation = relationship("Litigation", back_populates="opposing_parties")


# Create a model for the opposing party lawyer
class OpposingPartyLawyer(Base):
    __tablename__ = "opposing_party_lawyers"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    opposing_party_id = Column(String, ForeignKey("opposing_parties.id"))
    opposing_party = relationship("OpposingParty", backref="lawyers")
