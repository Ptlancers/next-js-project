import os
from .settings import settings
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Protection
from datetime import datetime
import pandas as pd


def replace_dashes_with_space(data: dict[str, str]) -> dict[str, str]:
    res: dict[str, str] = {}
    for key, value in data.items():
        res[key.replace("_", " ").title().strip()] = value
    return res


def get_month_and_year(date_string: str) -> tuple[str, int]:
    try:
        date_object: datetime = datetime.strptime(date_string, "%d-%m-%Y")
        month: str = date_object.strftime("%B")
        year: int = date_object.year
        return month, year
    except ValueError:
        return "Invalid date format", -1

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
    month, _ = get_month_and_year(datetime.now().strftime("%d-%m-%y"))
    wb = Workbook()
    for ws in wb.worksheets:
        ws.protection.sheet = True
        ws.protection.password = settings.password
    wb.save(filepath)


def create_excel_sheet(wb: Workbook, sheet_name: str, titles: list[str]):
    ws = wb.create_sheet(title=sheet_name)
    ws.append(titles)


def append_data_into_excel(data: dict, section_code: str) -> None:
    if not os.path.exists(settings.excelFolderPath) and settings.excelFolderPath == "":
        find_documents_folder()

    month, year = get_month_and_year(data["date"])

    file_path = os.path.join(settings.excelFolderPath, f"{section_code}-receipt-{year}.xlsx")

    if not os.path.exists(file_path):
        create_excel_file(file_path)

    wb = load_workbook(file_path)
    sheet_name:str = month
    if sheet_name not in wb.sheetnames:
        titles: list[str] = ["Serial Number"] + list(replace_dashes_with_space(data).keys())
        create_excel_sheet(wb, sheet_name, titles)

    ws = wb[sheet_name]
    data_with_serial = {"Serial Number": len(ws['A'])}
    data_with_serial.update(data)

    df = pd.DataFrame([data_with_serial])

    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)

    for row in ws.iter_rows(min_row=len(ws['A']) + 1, max_row=len(ws['A']) + len(df), max_col=len(titles)):
        for cell in row:
            cell.protection = Protection(locked=True)

    for ws in wb.worksheets:
        ws.protection.sheet = True
        ws.protection.password = settings.password

    wb.save(file_path)


def update_data_into_excel(data: dict, section_code: str, receipt_number: str) -> None:
    if not os.path.exists(settings.excelFolderPath) or settings.excelFolderPath == "":
        find_documents_folder()

    month, year = get_month_and_year(data.get("date"))
    file_path = os.path.join(settings.excelFolderPath, f"{section_code}-receipt-{year}.xlsx")

    if not os.path.exists(file_path):
        create_excel_file(file_path)

    wb = load_workbook(file_path)
    sheet_name: str = month
    ws = wb[sheet_name]

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=2, max_col=ws.max_column):
        if row[2].value == receipt_number:
            for cell in row:
                cell.value = data.get(cell.column_letter)

            for cell in row:
                cell.protection = Protection(locked=True)

            wb.save(file_path)
            return
