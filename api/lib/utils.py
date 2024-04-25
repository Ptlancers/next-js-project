from datetime import datetime, date


def replace_dashes_with_space(data: dict[str, str]) -> dict[str, str]:
    res: dict[str, str] = {}
    for key, value in data.items():
        res[key.replace("_", " ").title().strip()] = value
    return res


def clean_date_format(date_string: str | datetime) -> str:
    if isinstance(date_string, str):
        date_object: date = string_to_datetime(date_string)
    else:
        date_object: date = date_string.date()
    date_str = date_object.strftime("%d-%m-%Y")
    return date_str


def string_to_datetime(date_string: str) -> date:
    date_object: date = datetime.strptime(date_string, "%Y-%m-%d").date()
    return date_object


def get_month_and_year(date_string: str) -> tuple[str, int]:
    try:
        date_object: date = string_to_datetime(date_string)
        month: str = date_object.strftime("%B")
        year: int = date_object.year
        return month, year
    except ValueError:
        return "Invalid date format", -1
