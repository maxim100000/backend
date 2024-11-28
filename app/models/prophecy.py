from sqlmodel import SQLModel, Field


class ProphecyBase(SQLModel):
    content: str
    used: bool = False
    id: int | None = Field(default=None, primary_key=True)


class Prophecy(ProphecyBase, table=True):
    pass