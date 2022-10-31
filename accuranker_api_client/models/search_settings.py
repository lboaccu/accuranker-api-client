from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.default_search_setting_search_engine import DefaultSearchSettingSearchEngine
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSettings")

@attr.s(auto_attribs=True)
class SearchSettings:
    """
    Attributes:
        countrylocale (str): Two letters combination of country and language. Example: en-GB (for english in Great
            Britain)
        search_engine_names (List[DefaultSearchSettingSearchEngine]): List of search engines and search types
        locations (Union[Unset, List[str]]): List of specific locations. These are not validated, but if you are in
            doubt use google maps to verify. Example: London, United Kingdom
    """

    countrylocale: str
    search_engine_names: List[DefaultSearchSettingSearchEngine]
    locations: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        countrylocale = self.countrylocale
        search_engine_names = []
        for search_engine_names_item_data in self.search_engine_names:
            search_engine_names_item = search_engine_names_item_data.to_dict()

            search_engine_names.append(search_engine_names_item)




        locations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "countrylocale": countrylocale,
            "search_engine_names": search_engine_names,
        })
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        countrylocale = d.pop("countrylocale")

        search_engine_names = []
        _search_engine_names = d.pop("search_engine_names")
        for search_engine_names_item_data in (_search_engine_names):
            search_engine_names_item = DefaultSearchSettingSearchEngine.from_dict(search_engine_names_item_data)



            search_engine_names.append(search_engine_names_item)


        locations = cast(List[str], d.pop("locations", UNSET))


        search_settings = cls(
            countrylocale=countrylocale,
            search_engine_names=search_engine_names,
            locations=locations,
        )

        search_settings.additional_properties = d
        return search_settings

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
