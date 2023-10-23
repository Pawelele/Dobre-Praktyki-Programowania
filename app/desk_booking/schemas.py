from fastapi import HTTPException, status
from pydantic import BaseModel, validator
from desk_booking.exceptions import NegativeNumberException


class Desk(BaseModel):
    desk_type: str
    desk_number: int

    @validator("desk_number")
    def validate_desk_number(cls, desk_number):
        print("validator")
        if desk_number <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="There are no desks available with negative id"
            )
