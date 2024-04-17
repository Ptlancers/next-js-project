from pydantic import BaseModel


class Receipt(BaseModel):
    id: str = ""
    date: str
    donor_registration_number: str
    receipt_number: str = ""
    donor_name: str = ""
    unique_identification_number: str = ""
    address: str = ""
    donation_type: str = "corpus"
    mode_of_receipt: str = "cash"
    transaction_id: str = ""
    donated_amount: str
    donated_amount_letters: str


class SearchResponse(Receipt):
    pass


class InsertResponse(BaseModel):
    detail: str
    id: str


class UpdateResponse(InsertResponse):
    pass


class Section(BaseModel):
    section_code: str
    unique_registration_number: str
    date_insurance_of_urn: str
