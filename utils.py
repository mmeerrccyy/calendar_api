from datetime import date, datetime
from calendar_requests import get_api_contries, get_api_holidays
from fastapi import HTTPException, status

        
def get_api_iso_countries_list() -> list[str]:
    return [country_obj["iso-3166"].lower() for country_obj in get_api_contries()["countries"]]

def validate_iso_countries(validate_list: list[str]) -> None:
    valid_countries: list[str] = get_api_iso_countries_list()
    not_valid_countries: list[str] = [country_el for country_el in validate_list if country_el.lower() not in valid_countries]
    if not_valid_countries:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"""
            Got invalid countries: {','.join(not_valid_countries)}
            """)

def get_api_holidays_list(country: str, year: int) -> list[dict[str, str | int | None | dict]]:
    return [holiday_obj for holiday_obj in get_api_holidays(country=country, year=year)["holidays"]]


def filter_holidays_by_date(start_date: date, end_date: date, holidays: list[dict[str, str | int | None | dict]]):
    return [
        holiday for holiday in holidays
        if start_date <= datetime.fromisoformat(holiday['date']['iso']).date() <= end_date
    ]
