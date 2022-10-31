from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.search_settings import SearchSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordIn")

@attr.s(auto_attribs=True)
class KeywordIn:
    """
    Attributes:
        domain_id (int): Id of the domain you want to add the keywords to
        keywords (List[str]): List of keyword to add to the domain
        ignore_local_results (Union[Unset, bool]): Whether or not ranking on this keyword will ignore local results.
        ignore_featured_snippet (Union[Unset, bool]): Whether or not ranking on this keyword will ignore featured
            snippets.
        ignore_in_share_of_voice (Union[Unset, bool]): Whether or not this keyword should be ignored in aggregated share
            of voice
        starred (Union[Unset, bool]): Mark the keyword as starred
        description (Union[Unset, str]): Description of the keyword
        tags (Union[Unset, List[str]]): List of tags for the keyword. Used for filtering or grouping
        enable_autocorrect (Union[Unset, bool]): Enable autocorrect for searches on this keyword
        searchsettings (Union[Unset, List[SearchSettings]]): List of search settings to use on this keyword
    """

    domain_id: int
    keywords: List[str]
    ignore_local_results: Union[Unset, bool] = False
    ignore_featured_snippet: Union[Unset, bool] = False
    ignore_in_share_of_voice: Union[Unset, bool] = False
    starred: Union[Unset, bool] = False
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    enable_autocorrect: Union[Unset, bool] = False
    searchsettings: Union[Unset, List[SearchSettings]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        domain_id = self.domain_id
        keywords = self.keywords




        ignore_local_results = self.ignore_local_results
        ignore_featured_snippet = self.ignore_featured_snippet
        ignore_in_share_of_voice = self.ignore_in_share_of_voice
        starred = self.starred
        description = self.description
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        enable_autocorrect = self.enable_autocorrect
        searchsettings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.searchsettings, Unset):
            searchsettings = []
            for searchsettings_item_data in self.searchsettings:
                searchsettings_item = searchsettings_item_data.to_dict()

                searchsettings.append(searchsettings_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "domain_id": domain_id,
            "keywords": keywords,
        })
        if ignore_local_results is not UNSET:
            field_dict["ignore_local_results"] = ignore_local_results
        if ignore_featured_snippet is not UNSET:
            field_dict["ignore_featured_snippet"] = ignore_featured_snippet
        if ignore_in_share_of_voice is not UNSET:
            field_dict["ignore_in_share_of_voice"] = ignore_in_share_of_voice
        if starred is not UNSET:
            field_dict["starred"] = starred
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if enable_autocorrect is not UNSET:
            field_dict["enable_autocorrect"] = enable_autocorrect
        if searchsettings is not UNSET:
            field_dict["searchsettings"] = searchsettings

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        domain_id = d.pop("domain_id")

        keywords = cast(List[str], d.pop("keywords"))


        ignore_local_results = d.pop("ignore_local_results", UNSET)

        ignore_featured_snippet = d.pop("ignore_featured_snippet", UNSET)

        ignore_in_share_of_voice = d.pop("ignore_in_share_of_voice", UNSET)

        starred = d.pop("starred", UNSET)

        description = d.pop("description", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        enable_autocorrect = d.pop("enable_autocorrect", UNSET)

        searchsettings = []
        _searchsettings = d.pop("searchsettings", UNSET)
        for searchsettings_item_data in (_searchsettings or []):
            searchsettings_item = SearchSettings.from_dict(searchsettings_item_data)



            searchsettings.append(searchsettings_item)


        keyword_in = cls(
            domain_id=domain_id,
            keywords=keywords,
            ignore_local_results=ignore_local_results,
            ignore_featured_snippet=ignore_featured_snippet,
            ignore_in_share_of_voice=ignore_in_share_of_voice,
            starred=starred,
            description=description,
            tags=tags,
            enable_autocorrect=enable_autocorrect,
            searchsettings=searchsettings,
        )

        keyword_in.additional_properties = d
        return keyword_in

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
