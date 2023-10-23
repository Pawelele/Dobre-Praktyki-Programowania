from fastapi import APIRouter, HTTPException

from desk_booking.schemas import Desk
from desk_booking.enums import DeskTypeEnum
from desk_booking.service import BookingService

router = APIRouter(prefix="/desk_booking", tags=["desk_booking"])


@router.get("/book/{number}/{desk_type}")
async def book(number: int, desk_type: DeskTypeEnum) -> dict[str, str]:
    """
    Booking desk endpoint.
    :param number: desk identification number
    :param desk_type: type of desk (ordered from list - CLASSIC, REGULATED)
    :return: information about result of operation
    """
    try:
        BookingService().make_reservation(desk=Desk(desk_type=desk_type, desk_number=number))
        return {"message": "Reservation completed!"}
    except HTTPException as exc:
        return {"exc": str(exc.detail)}
