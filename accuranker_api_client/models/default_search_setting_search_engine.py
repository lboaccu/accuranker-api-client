from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.search_engine_enum import SearchEngineEnum
from ..models.search_type_enum import SearchTypeEnum

T = TypeVar("T", bound="DefaultSearchSettingSearchEngine")

@attr.s(auto_attribs=True)
class DefaultSearchSettingSearchEngine:
    """
    Attributes:
        search_engine (SearchEngineEnum): An enumeration.
        search_type_names (List[SearchTypeEnum]): List of search types.
    """

    search_engine: SearchEngineEnum
    search_type_names: List[SearchTypeEnum]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        search_engine = self.search_engine.value

        search_type_names = []
        for search_type_names_item_data in self.search_type_names:
            search_type_names_item = search_type_names_item_data.value

            search_type_names.append(search_type_names_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "search_engine": search_engine,
            "search_type_names": search_type_names,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        search_engine = SearchEngineEnum(d.pop("search_engine"))




        search_type_names = []
        _search_type_names = d.pop("search_type_names")
        for search_type_names_item_data in (_search_type_names):
            search_type_names_item = SearchTypeEnum(search_type_names_item_data)



            search_type_names.append(search_type_names_item)


        default_search_setting_search_engine = cls(
            search_engine=search_engine,
            search_type_names=search_type_names,
        )

        default_search_setting_search_engine.additional_properties = d
        return default_search_setting_search_engine

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
