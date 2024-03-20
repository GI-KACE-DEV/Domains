from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from app.db.base_class import APIBase, Base, UUID, Base
from .comment import Comment
from .action import Action
from .document import Document
from .attachment import Attachment


class HasComment:
    """HasComment mixin, creates a new Comment class
    for each parent.
    """

    @declared_attr
    def comments(cls):
        cls.Comment = type(
            "%s_Comment" % cls.__name__,
            (Comment, Base),
            dict(
                __tablename__="%s_comments" % cls.__tablename__,
                parent_id=Column(
                    UUID, ForeignKey("%s.id" % cls.__tablename__)
                ),
                parent=relationship(cls),
            ),
        )
        return relationship(cls.Comment)


class HasAction:
    """HasAction mixin, creates a new Action class
    for each parent.
    """

    @declared_attr
    def actions(cls):
        cls.Action = type(
            "%s_Action" % cls.__name__,
            (Action, APIBase),
            dict(
                __tablename__="%s_actions" % cls.__tablename__,
                parent_id=Column(
                    UUID, ForeignKey("%s.id" % cls.__tablename__)
                ),
                parent=relationship(cls),
            ),
        )
        return relationship(cls.Action)


class HasDocument:
    """HasDocument mixin, creates a new Document class
    for each parent.
    """

    @declared_attr
    def documents(cls):
        cls.Document = type(
            "%s_Document" % cls.__name__,
            (Document, APIBase),
            dict(
                __tablename__="%s_documents" % cls.__tablename__,
                parent_id=Column(
                    UUID, ForeignKey("%s.id" % cls.__tablename__)
                ),
                parent=relationship(cls),
            ),
        )
        return relationship(cls.Document)


class HasAttachement:
    """HasEvent mixin, creates a new Event class
    for each parent.
    """

    @declared_attr
    def documents(cls):
        cls.Document = type(
            "%sDocument" % cls.__name__,
            (Document, APIBase),
            dict(
                __tablename__="%s_documents" % cls.__tablename__,
                parent_id=Column(
                    UUID, ForeignKey("%s.id" % cls.__tablename__)
                ),
                parent=relationship(cls),
            ),
        )
        return relationship(cls.Document)


'''

'''
