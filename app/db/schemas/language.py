from pydantic import BaseModel, constr


class Language(BaseModel):
    name: constr(max_length=15)
