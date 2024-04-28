from sqlmodel import SQLModel, Field, Relationship
from typing import Optional 

class Transactions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: int = Field(default=None, nullable=False)
    category: str = Field(default=None, nullable=False)
    description: str = Field(default=None, nullable=False)
    is_income: bool = Field(default=False, nullable=False)
    date: str = Field(default=None, nullable=False)



    # user: "XXXXX" = Relationship(back_populates="transactions")