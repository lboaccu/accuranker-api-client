import datetime

from typing import Any, Dict, List, Type, TypeVar, Union, NamedTuple

import attr
from dateutil.parser import isoparse

from ..models.search_volume_history import SearchVolumeHistory
from ..types import UNSET, Unset

T = TypeVar("T", bound="LandingPageSerializerSchema")

class LandingPageSerializerSchemaFields(NamedTuple):
    id="id"
    path="path"
    created_at="created_at"
    history="history"
    additional_properties="additional_properties"

@attr.s(auto_attribs=True)
class LandingPageSerializerSchema:
    """
    Attributes:
        id (Union[Unset, int]):
        path (Union[Unset, None, str]):
        created_at (Union[Unset, datetime.date]):
        history (Union[Unset, List[SearchVolumeHistory]]):
    """

    id: Union[Unset, int] = UNSET
    path: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, datetime.date] = UNSET
    history: Union[Unset, List[SearchVolumeHistory]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        path = self.path
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()

                history.append(history_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        path = d.pop("path", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()




        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in (_history or []):
            history_item = SearchVolumeHistory.from_dict(history_item_data)



            history.append(history_item)


        landing_page_serializer_schema = cls(
            id=id,
            path=path,
            created_at=created_at,
            history=history,
        )

        landing_page_serializer_schema.additional_properties = d
        return landing_page_serializer_schema

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
