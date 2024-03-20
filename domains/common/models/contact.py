from sqlalchemy import (Column, String, Text, Boolean, Date, Table, ForeignKey)
from sqlalchemy.orm import relationship
from app.db.base_class import APIBase, UUID
from app.db.base_class import Base
from app.domains.common.models.utils import COUNTRIES


contacts_addresses = Table(
    'contact_addresses', Base.metadata,
    Column('contact_id', UUID, ForeignKey('contacts.id'), primary_key=True),
    Column('address_id', UUID, ForeignKey('addresses.id'),  primary_key=True)

)


class Country(APIBase):

    code = Column(String(4))
    country = Column(String(250))

    addresses = relationship("Address", back_populates="country")

    def __str__(self):
        return self.country()


class Address(APIBase):

    address_line1 = Column(String(255), nullable=True, default="")
    address_line2 = Column(String(255), nullable=True, default="")
    street = Column(String(255), nullable=True, default="")
    city = Column(String(255), nullable=True, default="")
    region_state = Column(String(255), nullable=True,  default="")
    postcode = Column(String(64),   default="", nullable=True)
    ghana_post = Column(String(64),  default="", nullable=True)
    p_o_box = Column(String(64),  nullable=True, default="")
    country_id = Column(UUID, ForeignKey("countries.id"))
    country = relationship("Country", back_populates="addresses")

    def __str__(self):
        return self.city if self.city else ""

    def get_complete_address(self):
        address = ""
        if self.address_line1:
            address += self.address_line1

        if self.address_line2:
            address += self.address_line2

        if self.street:
            if address:
                address += ", " + self.street
            else:
                address += self.street
        if self.city:
            if address:
                address += ", " + self.city
            else:
                address += self.city
        if self.state:
            if address:
                address += ", " + self.state
            else:
                address += self.state
        if self.postcode:
            if address:
                address += ", " + self.postcode
            else:
                address += self.postcode
        if self.postcode:
            if address:
                address += ", " + self.postcode
            else:
                address += self.postcode
        if self.country:
            if address:
                address += ", " + self.country  # self.get_country_display()
            else:
                address += self.country
        #    else:
        #        address += self.get_country_display()

        return address


class Contact(APIBase):

    salutation = Column(String(250), nullable=True)
    title = Column(String(250), nullable=True)
    description = Column(Text, nullable=True)
    first_name = Column(String(300))
    middle_name = Column(String(300), nullable=True)
    last_name = Column(String(300), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    personal_email = Column(String(250), unique=True)
    primary_official_email = Column(String(250), nullable=True)
    secondary_official_email = Column(String(250), nullable=True)
    primary_mobile_number = Column(String(20), nullable=True)
    secondary_mobile_number = Column(String(20), nullable=True)
    home_phone_number = Column(String(20), nullable=True)
    primary_office_phone_number = Column(String(20), nullable=True)
    secondary_office_phone_number = Column(String(20), nullable=True)
    department = Column(String(250), nullable=True)
    language = Column(String(250), nullable=True)
    do_not_call = Column(Boolean, default=True)
    website_url = Column(String(250), nullable=True)
    linked_in_url = Column(String(250), nullable=True)
    facebook_url = Column(String(250), nullable=True)
    twitter_username = Column(String(250), nullable=True)
    country = Column(String(250), nullable=True)
    is_active = Column(Boolean, default=True)

    creator_id = Column(UUID, ForeignKey("staffs.id"), nullable=True)

    # staff
    staffs = relationship("Staff", secondary="staffs_contacts",
                          back_populates="contacts")

    # client
    clients = relationship("Client", secondary="clients_contacts",
                           back_populates="contacts")

    # action
    actions = relationship("Action", secondary="action_contacts",
                           back_populates="contacts")

    # lead
    leads = relationship("Lead", secondary="leads_contacts",
                         back_populates="contacts")

    # consultation
    consultations = relationship("Consultation", secondary="consultations_contacts",
                                 back_populates="contacts")

    # brief
    # briefs = relationship("Brief", secondary="briefs_contacts",
    #                      back_populates="contacts")

    # litigation
    # litigations = relationship("Consultation",  secondary="consultations_contacts",
    #                           back_populates="contacts")

    def __str__(self):
        return f"{self.title} {self.name}"

    @property
    def name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
