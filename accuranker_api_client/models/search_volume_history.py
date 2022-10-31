import datetime

from typing import Any, Dict, List, Type, TypeVar, Union, NamedTuple

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchVolumeHistory")

class SearchVolumeHistoryFields(NamedTuple):
    search_volume = "search_volume"
    date = "date"


@attr.s(auto_attribs=True)
class SearchVolumeHistory:
    """
    Attributes:
        search_volume (Union[Unset, int]):
        date (Union[Unset, datetime.date]):
    """

    search_volume: Union[Unset, int] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        search_volume = self.search_volume
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if search_volume is not UNSET:
            field_dict["search_volume"] = search_volume
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_volume = d.pop("search_volume", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        search_volume_history = cls(
            search_volume=search_volume,
            date=date,
        )

        search_volume_history.additional_properties = d
        return search_volume_history

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
