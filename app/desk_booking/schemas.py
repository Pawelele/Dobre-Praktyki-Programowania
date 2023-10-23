import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class Desk(BaseModel):
    """Desk model"""

    desk_type: str
    desk_number: int

    @validator("desk_number")
    def validate_desk_number(cls, desk_number: int):
        if desk_number <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="There are no desks available with negative id"
            )


class Reservation(BaseModel):
    start_date: datetime.datetime
    end_date: datetime.datetime
