from functools import wraps
from fastapi import HTTPException, status



def parse_response(func):
    @wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        response_data = func(*args, **kwargs)
        if response_data.status_code == 200:
            return response_data.json()["response"]
        else:
            raise HTTPException(
                status_code=status.HTTP_500_BAD_REQUEST,
                detail=f"""
                Error! Got {response_data.status_code} from external API.
                """
            )
    return wrapper