from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.search_volume_history import SearchVolumeHistory
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tag")

@attr.s(auto_attribs=True)
class Tag:
    """
    Attributes:
        tag (Union[Unset, str]):
        history (Union[Unset, List[SearchVolumeHistory]]):
    """

    tag: Union[Unset, str] = UNSET
    history: Union[Unset, List[SearchVolumeHistory]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        tag = self.tag
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
        if tag is not UNSET:
            field_dict["tag"] = tag
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        tag = d.pop("tag", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in (_history or []):
            history_item = SearchVolumeHistory.from_dict(history_item_data)



            history.append(history_item)


        tag = cls(
            tag=tag,
            history=history,
        )

        tag.additional_properties = d
        return tag

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
