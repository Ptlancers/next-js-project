from datetime import datetime, date


def replace_dashes_with_space(data: dict[str, str]) -> dict[str, str]:
    res: dict[str, str] = {}
    for key, value in data.items():
        res[key.replace("_", " ").title().strip()] = value
    return res


def string_to_datetime(date_string: str) -> date:
    date_object: date = datetime.strptime(date_string, '%Y-%m-%d').date()
    return date_object


def get_month_and_year(date_string: str) -> tuple[str, int]:
    try:
        date_object: date = string_to_datetime(date_string)
        month: str = date_object.strftime("%B")
        year: int = date_object.year
        return month, year
    except ValueError:
        return "Invalid date format", -1
