import os
from urllib.parse import urlencode

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

CALENDAR_TOKEN: str = os.environ["API_TOKEN"]
CALENDAR_API: str = "https://calendarific.com/api/v2/"


def get_authorized_api_endpoint(endpoint: str, query_params: dict[str, str | int] | None = None) -> str:
    
    url_string = f"{CALENDAR_API}{endpoint}?api_key={CALENDAR_TOKEN}"
    if query_params:
        url_string += "&" + urlencode(query=query_params)

    return url_string