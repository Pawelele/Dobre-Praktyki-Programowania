from enum import Enum


class DeskTypeEnum(str, Enum):
    """Enum describing desk type"""

    CLASSIC = "classic"
    REGULATED = "regulated"
