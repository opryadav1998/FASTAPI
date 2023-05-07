from pydantic import BaseModel


class user_input(BaseModel):
    operation: str
    x: float
    y: float


class tabl(BaseModel):
    pass