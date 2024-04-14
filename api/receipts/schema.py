from pydantic import BaseModel


class Receipt(BaseModel):
    id:str=""
    date: str
    donor_registration_number: str
    receipt_number: str = ""
    donor_name: str = ""
    unique_identification_number: str = ""
    address: str = ""
    donation_type: str = ""
    mode_of_receipt: str = ""
    transaction_id: str = ""
    donated_amount: str
    donated_amount_letters: str = ""

    class Config:
        from_attributes = True

class AllReceipt(BaseModel):
    data=list[Receipt]

class SearchResponse(Receipt):
    pass


class InsertResponse(BaseModel):
    detail: str
    id:str


class UpdateResponse(InsertResponse):
    pass


class Section(BaseModel):
    section_code: str
    unique_registration_number: str
    date_insurance_of_urn: str
