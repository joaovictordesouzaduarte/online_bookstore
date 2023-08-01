from pydantic import BaseModel, constr


class Genre(BaseModel):
    name: constr(max_length=60)
