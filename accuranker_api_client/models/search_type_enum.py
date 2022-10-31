from enum import Enum


class SearchTypeEnum(str, Enum):
    DESKTOP = "Desktop"
    MOBILE = "Mobile"

    def __str__(self) -> str:
        return str(self.value)
