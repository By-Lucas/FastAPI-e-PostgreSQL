from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CUrsoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True