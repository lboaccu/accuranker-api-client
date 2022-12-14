from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="DeleteKeywordInput")

@attr.s(auto_attribs=True)
class DeleteKeywordInput:
    """
    Attributes:
        keyword_ids (List[int]): Ids of the keyword you want to delete
    """

    keyword_ids: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        keyword_ids = self.keyword_ids





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keyword_ids": keyword_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        keyword_ids = cast(List[int], d.pop("keyword_ids"))


        delete_keyword_input = cls(
            keyword_ids=keyword_ids,
        )

        delete_keyword_input.additional_properties = d
        return delete_keyword_input

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
