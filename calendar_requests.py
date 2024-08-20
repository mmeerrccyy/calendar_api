from requests import Response
import requests
from config import get_authorized_api_endpoint
from custom_decorators import parse_response


@parse_response
def get_api_contries() -> dict[str, str | int | None]:
    api_response: Response = requests.get(get_authorized_api_endpoint(endpoint="countries"))
    return api_response

@parse_response
def get_api_holidays(country: str, year: int) -> dict[str, str | int | None]:
    api_response: Response = requests.get(get_authorized_api_endpoint(endpoint="holidays", query_params={"country": country, "year": year}))
    return api_response