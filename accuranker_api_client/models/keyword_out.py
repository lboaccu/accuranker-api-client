from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordOut")

@attr.s(auto_attribs=True)
class KeywordOut:
    """
    Attributes:
        keyword (str): The actual keyword that is used as a search phrase
        country (str): Country for searches on the keyword, eg. 'Denmark'
        language (str): Language for searches on the keyword, eg. 'Danish'
        search_engine (str): Name of search engine, eg. 'Google'
        search_type (str): Search type for the keyword, possible values 'Dekstop' or 'Mobile'
        id (Union[Unset, int]):
        location (Union[Unset, str]): A specific location to narrow down the search for this keyword, eg. 'London, UK'
    """

    keyword: str
    country: str
    language: str
    search_engine: str
    search_type: str
    id: Union[Unset, int] = UNSET
    location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        keyword = self.keyword
        country = self.country
        language = self.language
        search_engine = self.search_engine
        search_type = self.search_type
        id = self.id
        location = self.location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keyword": keyword,
            "country": country,
            "language": language,
            "search_engine": search_engine,
            "search_type": search_type,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        keyword = d.pop("keyword")

        country = d.pop("country")

        language = d.pop("language")

        search_engine = d.pop("search_engine")

        search_type = d.pop("search_type")

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        keyword_out = cls(
            keyword=keyword,
            country=country,
            language=language,
            search_engine=search_engine,
            search_type=search_type,
            id=id,
            location=location,
        )

        keyword_out.additional_properties = d
        return keyword_out

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
