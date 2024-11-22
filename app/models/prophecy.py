from sqlmodel import SQLModel, Field


class ProphecyBase(SQLModel):
    content: str
    used: bool = False


class Prophecy(ProphecyBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
