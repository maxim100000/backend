from sqlmodel import SQLModel, Field


class Prophecy(SQLModel, table=True):
    id: int = Field(primary_key=True)
    content: str
    used: bool
    
    