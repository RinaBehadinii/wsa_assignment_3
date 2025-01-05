import json

import requests
from pydantic import BaseModel, ValidationError

API_URL = "https://api.openalex.org/authors/A5023888391"


class InstitutionData(BaseModel):
    id: str
    display_name: str | None = None
    type: str | None = None
    country_code: str | None = None
    updated_date: str | None = None


class AuthorData(BaseModel):
    id: str
    display_name: str
    works_count: int
    cited_by_count: int
    orcid: str | None = None
    last_known_institution: InstitutionData | None = None


def validate_api_response():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        validated_data = AuthorData(**response.json())
        print("Response is valid!")
        print(json.dumps(validated_data.model_dump(), indent=2))
        return True
    except ValidationError as ve:
        print("Response validation failed:", ve.json(indent=2))
        return False
    except requests.exceptions.RequestException as e:
        print("Failed to fetch data. Error:", e)
        return False
