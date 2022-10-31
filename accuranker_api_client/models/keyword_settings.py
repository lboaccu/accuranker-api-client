from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSettings")

@attr.s(auto_attribs=True)
class KeywordSettings:
    """
    Attributes:
        keyword_ids (Union[List[int], int]): List of keyword to update
        domain_id (Union[Unset, int]): Id of the domain you want to move the keywords to
        ignore_local_results (Union[Unset, bool]): Whether or not ranking on this keyword will ignore local results.
        ignore_featured_snippet (Union[Unset, bool]): Whether or not ranking on this keyword will ignore featured
            snippets.
        ignore_in_share_of_voice (Union[Unset, bool]): Whether or not this keyword should be ignored in aggregated share
            of voice
        starred (Union[Unset, bool]): Mark the keyword as starred
        description (Union[Unset, str]): Description of the keyword
        tags (Union[Unset, List[str]]): List of tags for the keyword. Used for filtering or grouping
        enable_autocorrect (Union[Unset, bool]): Enable autocorrect for searches on this keyword
    """

    keyword_ids: Union[List[int], int]
    domain_id: Union[Unset, int] = UNSET
    ignore_local_results: Union[Unset, bool] = UNSET
    ignore_featured_snippet: Union[Unset, bool] = UNSET
    ignore_in_share_of_voice: Union[Unset, bool] = UNSET
    starred: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    enable_autocorrect: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        keyword_ids: Union[List[int], int]

        if isinstance(self.keyword_ids, list):
            keyword_ids = self.keyword_ids




        else:
            keyword_ids = self.keyword_ids


        domain_id = self.domain_id
        ignore_local_results = self.ignore_local_results
        ignore_featured_snippet = self.ignore_featured_snippet
        ignore_in_share_of_voice = self.ignore_in_share_of_voice
        starred = self.starred
        description = self.description
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        enable_autocorrect = self.enable_autocorrect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keyword_ids": keyword_ids,
        })
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
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

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        def _parse_keyword_ids(data: object) -> Union[List[int], int]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyword_ids_type_0 = cast(List[int], data)

                return keyword_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[int], int], data)

        keyword_ids = _parse_keyword_ids(d.pop("keyword_ids"))


        domain_id = d.pop("domain_id", UNSET)

        ignore_local_results = d.pop("ignore_local_results", UNSET)

        ignore_featured_snippet = d.pop("ignore_featured_snippet", UNSET)

        ignore_in_share_of_voice = d.pop("ignore_in_share_of_voice", UNSET)

        starred = d.pop("starred", UNSET)

        description = d.pop("description", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        enable_autocorrect = d.pop("enable_autocorrect", UNSET)

        keyword_settings = cls(
            keyword_ids=keyword_ids,
            domain_id=domain_id,
            ignore_local_results=ignore_local_results,
            ignore_featured_snippet=ignore_featured_snippet,
            ignore_in_share_of_voice=ignore_in_share_of_voice,
            starred=starred,
            description=description,
            tags=tags,
            enable_autocorrect=enable_autocorrect,
        )

        keyword_settings.additional_properties = d
        return keyword_settings

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
