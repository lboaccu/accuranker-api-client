from enum import Enum


class SearchEngineEnum(str, Enum):
    GOOGLE = "Google"
    BING = "Bing"
    BAIDU = "Baidu"
    YANDEX = "Yandex"
    YOUTUBE = "Youtube"

    def __str__(self) -> str:
        return str(self.value)
