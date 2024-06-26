import time

SECCHOICES = (
    ("ADVERTISING", "ADVERTISING"),
    ("AGRICULTURE", "AGRICULTURE"),
    ("APPAREL & ACCESSORIES", "APPAREL & ACCESSORIES"),
    ("AUTOMOTIVE", "AUTOMOTIVE"),
    ("BANKING", "BANKING"),
    ("BIOTECHNOLOGY", "BIOTECHNOLOGY"),
    ("BUILDING MATERIALS & EQUIPMENT", "BUILDING MATERIALS & EQUIPMENT"),
    ("CHEMICAL", "CHEMICAL"),
    ("COMPUTER", "COMPUTER"),
    ("EDUCATION", "EDUCATION"),
    ("ELECTRONICS", "ELECTRONICS"),
    ("ENERGY", "ENERGY"),
    ("ENTERTAINMENT & LEISURE", "ENTERTAINMENT & LEISURE"),
    ("FINANCE", "FINANCE"),
    ("FOOD & BEVERAGE", "FOOD & BEVERAGE"),
    ("GROCERY", "GROCERY"),
    ("HEALTHCARE", "HEALTHCARE"),
    ("INSURANCE", "INSURANCE"),
    ("LEGAL", "LEGAL"),
    ("MANUFACTURING", "MANUFACTURING"),
    ("PUBLISHING", "PUBLISHING"),
    ("REAL ESTATE", "REAL ESTATE"),
    ("SERVICE", "SERVICE"),
    ("SOFTWARE", "SOFTWARE"),
    ("SPORTS", "SPORTS"),
    ("TECHNOLOGY", "TECHNOLOGY"),
    ("TELECOMMUNICATIONS", "TELECOMMUNICATIONS"),
    ("TELEVISION", "TELEVISION"),
    ("TRANSPORTATION", "TRANSPORTATION"),
    ("VENTURE CAPITAL", "VENTURE CAPITAL"),
)

TYPECHOICES = (
    ("CUSTOMER", "CUSTOMER"),
    ("INVESTOR", "INVESTOR"),
    ("PARTNER", "PARTNER"),
    ("RESELLER", "RESELLER"),
)

ROLES = (
    ("ADMIN", "ADMIN"),
    ("USER", "USER"),
)

LEAD__OPPORTUNITY_STATUS = (
    ("assigned", "Assigned"),
    ("in process", "In Process"),
    ("converted", "Converted"),
    ("recycled", "Recycled"),
    ("closed", "Closed"),
)

LEAD_OPPORTUNITY_SOURCE = (
    ("call", "Call"),
    ("email", "Email"),
    ("existing customer", "Existing Customer"),
    ("partner", "Partner"),
    ("public relations", "Public Relations"),
    ("compaign", "Campaign"),
    ("other", "Other"),
)

STATUS_CHOICE = (
    ("New", "New"),
    ("Assigned", "Assigned"),
    ("Pending", "Pending"),
    ("Closed", "Closed"),
    ("Rejected", "Rejected"),
    ("Duplicate", "Duplicate"),
)

PRIORITY_CHOICE = (
    ("Low", "Low"),
    ("Normal", "Normal"),
    ("High", "High"),
    ("Urgent", "Urgent"),
)

SUPPORT_CASE_TYPE = (("Question", "Question"), ("Incident", "Incident"), ("Problem", "Problem"))

CRM_STAGES = (
    ("QUALIFICATION", "QUALIFICATION"),
    ("NEEDS ANALYSIS", "NEEDS ANALYSIS"),
    ("VALUE PROPOSITION", "VALUE PROPOSITION"),
    ("IDENTIFY DECISION MAKERS", "IDENTIFY DECISION MAKERS"),
    ("PERCEPTION ANALYSIS", "PERCEPTION ANALYSIS"),
    ("PROPOSAL/PRICE QUOTE", "PROPOSAL/PRICE QUOTE"),
    ("NEGOTIATION/REVIEW", "NEGOTIATION/REVIEW"),
    ("CLOSED WON", "CLOSED WON"),
    ("CLOSED LOST", "CLOSED LOST"),
)

SOURCES = (
    ("NONE", "NONE"),
    ("WALKIN", "WALKIN"),
    ("CALL", "CALL"),
    ("EMAIL", " EMAIL"),
    ("EXISTING CLIENT", "EXISTING CLIENT"),
    ("PARTNER", "PARTNER"),
    ("PUBLIC RELATIONS", "PUBLIC RELATIONS"),
    ("CAMPAIGN", "CAMPAIGN"),
    ("WEBSITE", "WEBSITE"),
    ("OTHER", "OTHER"),
)

EVENT_PARENT_TYPE = ((10, "Account"), (13, "Lead"), (14, "Opportunity"), (11, "Case"))

EVENT_STATUS = (
    ("Planned", "Planned"),
    ("Held", "Held"),
    ("Not Held", "Not Held"),
    ("Not Started", "Not Started"),
    ("Started", "Started"),
    ("Completed", "Completed"),
    ("Canceled", "Canceled"),
    ("Deferred", "Deferred"),
)


COUNTRIES = (
    ("GB", "United Kingdom"),
    ("AF", "Afghanistan"),
    ("AX", "Aland Islands"),
    ("AL", "Albania"),
    ("DZ", "Algeria"),
    ("AS", "American Samoa"),
    ("AD", "Andorra"),
    ("AO", "Angola"),
    ("AI", "Anguilla"),
    ("AQ", "Antarctica"),
    ("AG", "Antigua and Barbuda"),
    ("AR", "Argentina"),
    ("AM", "Armenia"),
    ("AW", "Aruba"),
    ("AU", "Australia"),
    ("AT", "Austria"),
    ("AZ", "Azerbaijan"),
    ("BS", "Bahamas"),
    ("BH", "Bahrain"),
    ("BD", "Bangladesh"),
    ("BB", "Barbados"),
    ("BY", "Belarus"),
    ("BE", "Belgium"),
    ("BZ", "Belize"),
    ("BJ", "Benin"),
    ("BM", "Bermuda"),
    ("BT", "Bhutan"),
    ("BO", "Bolivia"),
    ("BA", "Bosnia and Herzegovina"),
    ("BW", "Botswana"),
    ("BV", "Bouvet Island"),
    ("BR", "Brazil"),
    ("IO", "British Indian Ocean Territory"),
    ("BN", "Brunei Darussalam"),
    ("BG", "Bulgaria"),
    ("BF", "Burkina Faso"),
    ("BI", "Burundi"),
    ("KH", "Cambodia"),
    ("CM", "Cameroon"),
    ("CA", "Canada"),
    ("CV", "Cape Verde"),
    ("KY", "Cayman Islands"),
    ("CF", "Central African Republic"),
    ("TD", "Chad"),
    ("CL", "Chile"),
    ("CN", "China"),
    ("CX", "Christmas Island"),
    ("CC", "Cocos (Keeling) Islands"),
    ("CO", "Colombia"),
    ("KM", "Comoros"),
    ("CG", "Congo"),
    ("CD", "Congo, The Democratic Republic of the"),
    ("CK", "Cook Islands"),
    ("CR", "Costa Rica"),
    ("CI", "Cote d'Ivoire"),
    ("HR", "Croatia"),
    ("CU", "Cuba"),
    ("CY", "Cyprus"),
    ("CZ", "Czech Republic"),
    ("DK", "Denmark"),
    ("DJ", "Djibouti"),
    ("DM", "Dominica"),
    ("DO", "Dominican Republic"),
    ("EC", "Ecuador"),
    ("EG", "Egypt"),
    ("SV", "El Salvador"),
    ("GQ", "Equatorial Guinea"),
    ("ER", "Eritrea"),
    ("EE", "Estonia"),
    ("ET", "Ethiopia"),
    ("FK", "Falkland Islands (Malvinas)"),
    ("FO", "Faroe Islands"),
    ("FJ", "Fiji"),
    ("FI", "Finland"),
    ("FR", "France"),
    ("GF", "French Guiana"),
    ("PF", "French Polynesia"),
    ("TF", "French Southern Territories"),
    ("GA", "Gabon"),
    ("GM", "Gambia"),
    ("GE", "Georgia"),
    ("DE", "Germany"),
    ("GH", "Ghana"),
    ("GI", "Gibraltar"),
    ("GR", "Greece"),
    ("GL", "Greenland"),
    ("GD", "Grenada"),
    ("GP", "Guadeloupe"),
    ("GU", "Guam"),
    ("GT", "Guatemala"),
    ("GG", "Guernsey"),
    ("GN", "Guinea"),
    ("GW", "Guinea-Bissau"),
    ("GY", "Guyana"),
    ("HT", "Haiti"),
    ("HM", "Heard Island and McDonald Islands"),
    ("VA", "Holy See (Vatican City State)"),
    ("HN", "Honduras"),
    ("HK", "Hong Kong"),
    ("HU", "Hungary"),
    ("IS", "Iceland"),
    ("IN", "India"),
    ("ID", "Indonesia"),
    ("IR", "Iran, Islamic Republic of"),
    ("IQ", "Iraq"),
    ("IE", "Ireland"),
    ("IM", "Isle of Man"),
    ("IL", "Israel"),
    ("IT", "Italy"),
    ("JM", "Jamaica"),
    ("JP", "Japan"),
    ("JE", "Jersey"),
    ("JO", "Jordan"),
    ("KZ", "Kazakhstan"),
    ("KE", "Kenya"),
    ("KI", "Kiribati"),
    ("KP", "Korea, Democratic People's Republic of"),
    ("KR", "Korea, Republic of"),
    ("KW", "Kuwait"),
    ("KG", "Kyrgyzstan"),
    ("LA", "Lao People's Democratic Republic"),
    ("LV", "Latvia"),
    ("LB", "Lebanon"),
    ("LS", "Lesotho"),
    ("LR", "Liberia"),
    ("LY", "Libyan Arab Jamahiriya"),
    ("LI", "Liechtenstein"),
    ("LT", "Lithuania"),
    ("LU", "Luxembourg"),
    ("MO", "Macao"),
    ("MK", "Macedonia, The Former Yugoslav Republic of"),
    ("MG", "Madagascar"),
    ("MW", "Malawi"),
    ("MY", "Malaysia"),
    ("MV", "Maldives"),
    ("ML", "Mali"),
    ("MT", "Malta"),
    ("MH", "Marshall Islands"),
    ("MQ", "Martinique"),
    ("MR", "Mauritania"),
    ("MU", "Mauritius"),
    ("YT", "Mayotte"),
    ("MX", "Mexico"),
    ("FM", "Micronesia, Federated States of"),
    ("MD", "Moldova"),
    ("MC", "Monaco"),
    ("MN", "Mongolia"),
    ("ME", "Montenegro"),
    ("MS", "Montserrat"),
    ("MA", "Morocco"),
    ("MZ", "Mozambique"),
    ("MM", "Myanmar"),
    ("NA", "Namibia"),
    ("NR", "Nauru"),
    ("NP", "Nepal"),
    ("NL", "Netherlands"),
    ("AN", "Netherlands Antilles"),
    ("NC", "New Caledonia"),
    ("NZ", "New Zealand"),
    ("NI", "Nicaragua"),
    ("NE", "Niger"),
    ("NG", "Nigeria"),
    ("NU", "Niue"),
    ("NF", "Norfolk Island"),
    ("MP", "Northern Mariana Islands"),
    ("NO", "Norway"),
    ("OM", "Oman"),
    ("PK", "Pakistan"),
    ("PW", "Palau"),
    ("PS", "Palestinian Territory, Occupied"),
    ("PA", "Panama"),
    ("PG", "Papua New Guinea"),
    ("PY", "Paraguay"),
    ("PE", "Peru"),
    ("PH", "Philippines"),
    ("PN", "Pitcairn"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("PR", "Puerto Rico"),
    ("QA", "Qatar"),
    ("RE", "Reunion"),
    ("RO", "Romania"),
    ("RU", "Russian Federation"),
    ("RW", "Rwanda"),
    ("BL", "Saint Barthelemy"),
    ("SH", "Saint Helena"),
    ("KN", "Saint Kitts and Nevis"),
    ("LC", "Saint Lucia"),
    ("MF", "Saint Martin"),
    ("PM", "Saint Pierre and Miquelon"),
    ("VC", "Saint Vincent and the Grenadines"),
    ("WS", "Samoa"),
    ("SM", "San Marino"),
    ("ST", "Sao Tome and Principe"),
    ("SA", "Saudi Arabia"),
    ("SN", "Senegal"),
    ("RS", "Serbia"),
    ("SC", "Seychelles"),
    ("SL", "Sierra Leone"),
    ("SG", "Singapore"),
    ("SK", "Slovakia"),
    ("SI", "Slovenia"),
    ("SB", "Solomon Islands"),
    ("SO", "Somalia"),
    ("ZA", "South Africa"),
    ("GS", "South Georgia and the South Sandwich Islands"),
    ("ES", "Spain"),
    ("LK", "Sri Lanka"),
    ("SD", "Sudan"),
    ("SR", "Suriname"),
    ("SJ", "Svalbard and Jan Mayen"),
    ("SZ", "Swaziland"),
    ("SE", "Sweden"),
    ("CH", "Switzerland"),
    ("SY", "Syrian Arab Republic"),
    ("TW", "Taiwan, Province of China"),
    ("TJ", "Tajikistan"),
    ("TZ", "Tanzania, United Republic of"),
    ("TH", "Thailand"),
    ("TL", "Timor-Leste"),
    ("TG", "Togo"),
    ("TK", "Tokelau"),
    ("TO", "Tonga"),
    ("TT", "Trinidad and Tobago"),
    ("TN", "Tunisia"),
    ("TR", "Turkey"),
    ("TM", "Turkmenistan"),
    ("TC", "Turks and Caicos Islands"),
    ("TV", "Tuvalu"),
    ("UG", "Uganda"),
    ("UA", "Ukraine"),
    ("AE", "United Arab Emirates"),
    ("US", "United States"),
    ("UM", "United States Minor Outlying Islands"),
    ("UY", "Uruguay"),
    ("UZ", "Uzbekistan"),
    ("VU", "Vanuatu"),
    ("VE", "Venezuela"),
    ("VN", "Viet Nam"),
    ("VG", "Virgin Islands, British"),
    ("VI", "Virgin Islands, U.S."),
    ("WF", "Wallis and Futuna"),
    ("EH", "Western Sahara"),
    ("YE", "Yemen"),
    ("ZM", "Zambia"),
    ("ZW", "Zimbabwe")
)

CURRENCY_CODES = (
    ("AED", "AED, Dirham"),
    ("AFN", "AFN, Afghani"),
    ("ALL", "ALL, Lek"),
    ("AMD", "AMD, Dram"),
    ("ANG", "ANG, Guilder"),
    ("AOA", "AOA, Kwanza"),
    ("ARS", "ARS, Peso"),
    ("AUD", "AUD, Dollar"),
    ("AWG", "AWG, Guilder"),
    ("AZN", "AZN, Manat"),
    ("BAM", "BAM, Marka"),
    ("BBD", "BBD, Dollar"),
    ("BDT", "BDT, Taka"),
    ("BGN", "BGN, Lev"),
    ("BHD", "BHD, Dinar"),
    ("BIF", "BIF, Franc"),
    ("BMD", "BMD, Dollar"),
    ("BND", "BND, Dollar"),
    ("BOB", "BOB, Boliviano"),
    ("BRL", "BRL, Real"),
    ("BSD", "BSD, Dollar"),
    ("BTN", "BTN, Ngultrum"),
    ("BWP", "BWP, Pula"),
    ("BYR", "BYR, Ruble"),
    ("BZD", "BZD, Dollar"),
    ("CAD", "CAD, Dollar"),
    ("CDF", "CDF, Franc"),
    ("CHF", "CHF, Franc"),
    ("CLP", "CLP, Peso"),
    ("CNY", "CNY, Yuan Renminbi"),
    ("COP", "COP, Peso"),
    ("CRC", "CRC, Colon"),
    ("CUP", "CUP, Peso"),
    ("CVE", "CVE, Escudo"),
    ("CZK", "CZK, Koruna"),
    ("DJF", "DJF, Franc"),
    ("DKK", "DKK, Krone"),
    ("DOP", "DOP, Peso"),
    ("DZD", "DZD, Dinar"),
    ("EGP", "EGP, Pound"),
    ("ERN", "ERN, Nakfa"),
    ("ETB", "ETB, Birr"),
    ("EUR", "EUR, Euro"),
    ("FJD", "FJD, Dollar"),
    ("FKP", "FKP, Pound"),
    ("GBP", "GBP, Pound"),
    ("GEL", "GEL, Lari"),
    ("GHS", "GHS, Ghs"),
    ("GIP", "GIP, Pound"),
    ("GMD", "GMD, Dalasi"),
    ("GNF", "GNF, Franc"),
    ("GTQ", "GTQ, Quetzal"),
    ("GYD", "GYD, Dollar"),
    ("HKD", "HKD, Dollar"),
    ("HNL", "HNL, Lempira"),
    ("HRK", "HRK, Kuna"),
    ("HTG", "HTG, Gourde"),
    ("HUF", "HUF, Forint"),
    ("IDR", "IDR, Rupiah"),
    ("ILS", "ILS, Shekel"),
    ("INR", "INR, Rupee"),
    ("IQD", "IQD, Dinar"),
    ("IRR", "IRR, Rial"),
    ("ISK", "ISK, Krona"),
    ("JMD", "JMD, Dollar"),
    ("JOD", "JOD, Dinar"),
    ("JPY", "JPY, Yen"),
    ("KES", "KES, Shilling"),
    ("KGS", "KGS, Som"),
    ("KHR", "KHR, Riels"),
    ("KMF", "KMF, Franc"),
    ("KPW", "KPW, Won"),
    ("KRW", "KRW, Won"),
    ("KWD", "KWD, Dinar"),
    ("KYD", "KYD, Dollar"),
    ("KZT", "KZT, Tenge"),
    ("LAK", "LAK, Kip"),
    ("LBP", "LBP, Pound"),
    ("LKR", "LKR, Rupee"),
    ("LRD", "LRD, Dollar"),
    ("LSL", "LSL, Loti"),
    ("LTL", "LTL, Litas"),
    ("LVL", "LVL, Lat"),
    ("LYD", "LYD, Dinar"),
    ("MAD", "MAD, Dirham"),
    ("MDL", "MDL, Leu"),
    ("MGA", "MGA, Ariary"),
    ("MKD", "MKD, Denar"),
    ("MMK", "MMK, Kyat"),
    ("MNT", "MNT, Tugrik"),
    ("MOP", "MOP, Pataca"),
    ("MRO", "MRO, Ouguiya"),
    ("MUR", "MUR, Rupee"),
    ("MVR", "MVR, Rufiyaa"),
    ("MWK", "MWK, Kwacha"),
    ("MXN", "MXN, Peso"),
    ("MYR", "MYR, Ringgit"),
    ("MZN", "MZN, Metical"),
    ("NAD", "NAD, Dollar"),
    ("NGN", "NGN, Naira"),
    ("NIO", "NIO, Cordoba"),
    ("NOK", "NOK, Krone"),
    ("NPR", "NPR, Rupee"),
    ("NZD", "NZD, Dollar"),
    ("OMR", "OMR, Rial"),
    ("PAB", "PAB, Balboa"),
    ("PEN", "PEN, Sol"),
    ("PGK", "PGK, Kina"),
    ("PHP", "PHP, Peso"),
    ("PKR", "PKR, Rupee"),
    ("PLN", "PLN, Zloty"),
    ("PYG", "PYG, Guarani"),
    ("QAR", "QAR, Rial"),
    ("RON", "RON, Leu"),
    ("RSD", "RSD, Dinar"),
    ("RUB", "RUB, Ruble"),
    ("RWF", "RWF, Franc"),
    ("SAR", "SAR, Rial"),
    ("SBD", "SBD, Dollar"),
    ("SCR", "SCR, Rupee"),
    ("SDG", "SDG, Pound"),
    ("SEK", "SEK, Krona"),
    ("SGD", "SGD, Dollar"),
    ("SHP", "SHP, Pound"),
    ("SLL", "SLL, Leone"),
    ("SOS", "SOS, Shilling"),
    ("SRD", "SRD, Dollar"),
    ("SSP", "SSP, Pound"),
    ("STD", "STD, Dobra"),
    ("SYP", "SYP, Pound"),
    ("SZL", "SZL, Lilangeni"),
    ("THB", "THB, Baht"),
    ("TJS", "TJS, Somoni"),
    ("TMT", "TMT, Manat"),
    ("TND", "TND, Dinar"),
    ("TOP", "TOP, Paanga"),
    ("TRY", "TRY, Lira"),
    ("TTD", "TTD, Dollar"),
    ("TWD", "TWD, Dollar"),
    ("TZS", "TZS, Shilling"),
    ("UAH", "UAH, Hryvnia"),
    ("UGX", "UGX, Shilling"),
    ("USD", "$, Dollar"),
    ("UYU", "UYU, Peso"),
    ("UZS", "UZS, Som"),
    ("VEF", "VEF, Bolivar"),
    ("VND", "VND, Dong"),
    ("VUV", "VUV, Vatu"),
    ("WST", "WST, Tala"),
    ("XAF", "XAF, Franc"),
    ("XCD", "XCD, Dollar"),
    ("XOF", "XOF, Franc"),
    ("XPF", "XPF, Franc"),
    ("YER", "YER, Rial"),
    ("ZAR", "ZAR, Rand"),
    ("ZMK", "ZMK, Kwacha"),
    ("ZWL", "ZWL, Dollar"),
)


def return_complete_address(self):
    address = ""
    if self.address_line:
        address += self.address_line
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
    if self.country:
        if address:
            address += ", " + self.get_country_display()
        else:
            address += self.get_country_display()
    return address


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def convert_to_custom_timezone(custom_date, custom_timezone, to_utc=False):
    user_time_zone = pytz.timezone(custom_timezone)
    if to_utc:
        custom_date = user_time_zone.localize(custom_date.replace(tzinfo=None))
        user_time_zone = pytz.UTC
    return custom_date.astimezone(user_time_zone)


def append_str_to(append_to: str, *args, sep=", ", **kwargs):
    """Concatenate to a string.
    Args:
        append_to(str): The string to append to.
        args(list): list of string characters to concatenate.
        sep(str): Seperator to use between concatenated strings.
        kwargs(dict): Mapping of variables with intended string values.
    Returns:
        str, joined strings seperated
    """
    append_to = append_to or ""
    result_list = [append_to] + list(args) + list(kwargs.values())
    data = False
    for item in result_list:
        if item:
            data = True
            break
    return f"{sep}".join(filter(len, result_list)) if data else ""


def img_url(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" %(hash_, filename)


def dict_from_tuple(tuple):
    return dict( (x, y) for x, y in tuple)
