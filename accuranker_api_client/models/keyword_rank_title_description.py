from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordRankTitleDescription")

@attr.s(auto_attribs=True)
class KeywordRankTitleDescription:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        keyword_rank_title_description = cls(
            id=id,
            title=title,
            description=description,
        )

        keyword_rank_title_description.additional_properties = d
        return keyword_rank_title_description

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
