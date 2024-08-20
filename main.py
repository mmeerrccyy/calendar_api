import io
import zipfile
from datetime import date
import json

from fastapi import FastAPI, Query, Response
from fastapi.responses import FileResponse

from utils import filter_holidays_by_date, get_api_holidays_list, validate_iso_countries

app = FastAPI()

@app.get("/holidays", response_class=FileResponse)
def get_calendar_holidays(
    countries: str = Query(..., example="ua,us"),
    start_date: date = Query(..., example="2010-12-30"),
    end_date: date = Query(..., example="2018-12-30"),
) -> Response:
    zip_buffer = io.BytesIO()
    countries = countries.split(",")
    validate_iso_countries(countries)
    date_year = list(range(start_date.year, end_date.year + 1))
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for country in countries:
            country_holidays = []
            for year_el in date_year:
                country_holidays.extend(get_api_holidays_list(country=country, year=year_el))
            file_name = f"{country}_{start_date.day}-{start_date.month}-{start_date.year}_{end_date.day}-{end_date.month}-{end_date.year}.json"
            zip_file.writestr(file_name, json.dumps(filter_holidays_by_date(start_date=start_date, end_date=end_date, holidays=country_holidays)))

    zip_buffer.seek(0)

    return Response(
        content=zip_buffer.getvalue(),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=holidays.zip"}
    )
