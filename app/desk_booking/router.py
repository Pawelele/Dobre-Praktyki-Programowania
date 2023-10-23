from fastapi import APIRouter, HTTPException, Query

from desk_booking.schemas import Desk
from desk_booking.enums import DeskTypeEnum
from desk_booking.service import BookingService

router = APIRouter(prefix="/desk_booking", tags=["desk_booking"])


@router.get("/book/{number}/{desk_type}")
async def book(number: int, desk_type: DeskTypeEnum):
    try:
        BookingService.make_reservation(Desk(desk_type=desk_type, desk_number=number))
        return {"message": "not booked"}
    except HTTPException as exc:
        return {"exc": exc}
