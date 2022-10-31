from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_filter_filters_item import ApiFilterFiltersItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFilter")

@attr.s(auto_attribs=True)
class ApiFilter:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): The name of the filter.
        filters (Union[Unset, List[ApiFilterFiltersItem]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    filters: Union[Unset, List[ApiFilterFiltersItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()

                filters.append(filters_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in (_filters or []):
            filters_item = ApiFilterFiltersItem.from_dict(filters_item_data)



            filters.append(filters_item)


        api_filter = cls(
            id=id,
            name=name,
            filters=filters,
        )

        api_filter.additional_properties = d
        return api_filter

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
