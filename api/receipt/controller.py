from database.database import ReceiptDB as DB


def get_data_by_receipt_id(receipt_id: str) -> dict:
    receipt: dict = DB.get_receipt_by_id(receipt_id)
    return receipt


def get_data_by_receipt_number(receipt_number: str, section_code: str):
    receipt: dict = DB.get_receipt_by_receipt_no(receipt_number, section_code)
    return receipt


def check_receipt_no_exits(receipt_number: str, section_code: str) -> bool:
    receipt: dict = get_data_by_receipt_number(receipt_number, section_code)
    return bool(receipt)


def create_receipt(data: dict) -> str:
    new_receipt = DB.create_receipt(data)
    return new_receipt.get("id")

def update_receipt(receipt_id:str,data:dict)->str:
    updated_receipt = DB.update_receipt(receipt_id, data)
    return updated_receipt.get("id")