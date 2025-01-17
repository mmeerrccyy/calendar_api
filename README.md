## Task

```
With given start_time, end_time and countries_list as input, please create a solution
that will collect all holidays for provided countries between start_time and end_time from calendarific API.
Represent each holiday as Json string and store them in the files, divide files by country.

Calendarific API has Free Plan that makes code testing easy
Also, they have good documentation with all needed information for this challange
API Doc: https://calendarific.com/api-documentation

Input example:
countries_list = ['ua', 'us', 'gb'] 
start_time = datetime(year=1992, month=7, day=7)
start_time = datetime(year=1992, month=9, day=18)

You can find files with expected result for provided input example in 'expected_result' folder:
ua_7-7-1992_18-9-1992.txt
us_7-7-1992_18-9-1992.txt
gb_7-7-1992_18-9-1992.txt
```

## Configuration

`.env` file

```env
API_TOKEN=yourtoken
```


## Running code

### Without Docker

Run in terminal

```sh
poetry install

fastapi run
```

### With Docker

```sh
docker compose up
```