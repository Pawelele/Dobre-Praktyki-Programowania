
import pytest
from fastapi import HTTPException

from app.desk_booking.schemas import Desk
from tests.unit.test_constants import DESK_SAMPLES_CORRECT, DESK_SAMPLES_INCORRECT


@pytest.mark.parametrize("desk_params", DESK_SAMPLES_CORRECT)
def test_desk_correct(desk_params: dict[str, str | int]):
    desk = Desk(desk_number=desk_params["desk_number"], desk_type=desk_params["desk_type"])
    assert desk


@pytest.mark.parametrize("desk_params", DESK_SAMPLES_INCORRECT)
def test_desk_incorrect(desk_params: dict[str, str | int]):
    with pytest.raises(HTTPException):
        Desk(desk_number=desk_params["desk_number"], desk_type=desk_params["desk_type"])

