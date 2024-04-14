import os
from .settings import settings
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook, load_workbook
from datetime import datetime
import pandas as pd
import sys


def replace_dashes_with_space(data: dict):
    res = {}
    for key, value in data.items():
        res[key.replace("_", " ").title().strip()] = value
    return res


def find_documents_folder() -> None:
    home_directory: str = os.path.expanduser("~")

    possible_paths: list[str] = [
        os.path.join(home_directory, "Documents"),
        os.path.join(home_directory, "My Documents"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            receipt_data_path: str = os.path.join(path, "receipt data")

            if not os.path.exists(receipt_data_path):
                os.makedirs(receipt_data_path, exist_ok=True)
            settings.excelFolderPath = receipt_data_path
            settings.save_settings()
            return


def create_excel_file(filepath: str):
    wb = Workbook()
    ws = wb.active
    ws.protection.sheet = True
    wb.save(filepath)


def append_data_into_excel(data: dict, section_code: str):
    if not os.path.exists(settings.excelFolderPath) and settings.excelFolderPath == "":
        find_documents_folder()

    file_path = os.path.join(settings.excelFolderPath, f"{section_code}-receipt-{datetime.now().year}.xlsx")
    if not os.path.exists(file_path):
        create_excel_file(file_path)

    wb = load_workbook(file_path)
    month_sheet_name = datetime.now().strftime("%B")
    if month_sheet_name not in wb.sheetnames:
        ws = wb.create_sheet(title=month_sheet_name)
        ws.append(["Serial Number"] + list(replace_dashes_with_space(data).keys()))  # Add column headers

    else:
        ws = wb[month_sheet_name]

    # Add serial numbers to data dictionary
    data_with_serial = {"Serial Number": len(ws['A'])}  # Using length of column A as the serial number
    data_with_serial.update(data)

    df = pd.DataFrame([data_with_serial])  # Convert data dictionary to DataFrame
    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)
    ws.protection.sheet = True
    wb.save(file_path)




def update_data_into_excel(data: dict, section_code: str, receipt_number: str):
    """
    Updates data in an Excel file based on the section code and receipt number.

    Parameters:
    - data (dict): The data to update.
    - section_code (str): The section code to identify the data.
    - receipt_number (str): The receipt number to identify the data.

    Returns:
    - None
    """
    if not os.path.exists(settings.excelFolderPath) or settings.excelFolderPath == "":
        find_documents_folder()

    file_path = os.path.join(settings.excelFolderPath, f"{section_code}-receipt-{datetime.now().year}.xlsx")
    if not os.path.exists(file_path):
        create_excel_file(file_path)

    wb = load_workbook(file_path)

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=2, max_col=ws.max_column):
            if row[2].value == receipt_number:
                for cell in row:
                    cell.value = list(data.values())[cell.column-2]
                ws.protection.sheet = True
                wb.save(file_path)
                return




# append_data_into_excel({'date': '', 'donor_registration_number': '', 'receipt_number': '16', 'donor_name': 'vijaykumar',
#                         'unique_identification_number': '', 'address': '', 'donation_type': '', 'mode_of_receipt': '',
#                         'transaction_id': '', 'donated_amount': '2000000', 'donated_amount_letters': '',
#                         'section_code': '1234', 'unique_registration_number': '445678',
#                         'date_insurance_of_urn': '2024-04-04'}, "1234")


# update_data_into_excel(
#     {'date': '15', 'donor_registration_number': '', 'receipt_number': '16', 'donor_name': 'vijayakumar',
#      'unique_identification_number': '', 'address': '', 'donation_type': '', 'mode_of_receipt': '',
#      'transaction_id': '', 'donated_amount': '2000000', 'donated_amount_letters': '',
#      'section_code': '1234', 'unique_registration_number': '445678',
#      'date_insurance_of_urn': '2024-04-04'}, "1234", "16"
# )