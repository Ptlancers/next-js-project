from database.database import ReceiptDB as R_DB, DonorDB as D_DB

from . import schema


def get_data_by_receipt_id(receipt_id: str) -> dict:
    receipt: dict = R_DB.get_receipt_by_id(receipt_id)
    return receipt


def get_data_by_receipt_number(receipt_number: str, section_code: str):
    receipt: dict = R_DB.get_receipt_by_receipt_no(receipt_number, section_code)
    return receipt


def check_receipt_no_exits(receipt_number: str, section_code: str) -> bool:
    receipt: dict = get_data_by_receipt_number(receipt_number, section_code)
    return bool(receipt)


def create_receipt(data: dict) -> str:
    donor_data: dict = schema.DonorDetail(**data).dict()
    if not D_DB.read(donor_data.get("unique_identification_number")):
        create_receipt(donor_data)
    else:
        D_DB.update(donor_data)
    new_receipt = R_DB.create_receipt(data)
    return new_receipt.get("id")


def update_receipt(receipt_id: str, data: dict) -> str:
    donor_data: dict = schema.DonorDetail(**data).dict()
    if not D_DB.read(donor_data.get("unique_identification_number")):
        create_receipt(donor_data)
    else:
        D_DB.update(donor_data)
    updated_receipt = R_DB.update_receipt(receipt_id, data)
    return updated_receipt.get("id")


def read_donor_detail(key: str) -> dict:
    return D_DB.read(key)
