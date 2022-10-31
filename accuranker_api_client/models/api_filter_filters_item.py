from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFilterFiltersItem")

@attr.s(auto_attribs=True)
class ApiFilterFiltersItem:
    """
    Attributes:
        type (Union[Unset, str]): Can be: `string`, `num`, `array`, `list`, `bool` and `datetime`
        value (Union[Unset, str]): Please note that an array will be in a string: `"['1', '2']"`
        attribute (Union[Unset, str]):
        comparison (Union[Unset, str]):
            Depended on the type:
            * string: `contains`, `not_contains`, `starts_with`, `ends_with`, `eq` and `ne`
            * num: `gt`, `gte`, `lt`, `lte`, `eq` and `between`
            * array: `any`, `all` and `none`
            * list: `contains`
            * bool: `eq` and  `ne`
            * datetime: `gt`, `gte`, `lt`, `lte`, `eq` and `between`
    """

    type: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    attribute: Union[Unset, str] = UNSET
    comparison: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        value = self.value
        attribute = self.attribute
        comparison = self.comparison

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if comparison is not UNSET:
            field_dict["comparison"] = comparison

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        type = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        attribute = d.pop("attribute", UNSET)

        comparison = d.pop("comparison", UNSET)

        api_filter_filters_item = cls(
            type=type,
            value=value,
            attribute=attribute,
            comparison=comparison,
        )

        api_filter_filters_item.additional_properties = d
        return api_filter_filters_item

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
