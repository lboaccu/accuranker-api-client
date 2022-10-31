from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.search_settings import SearchSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSchemaOut")

@attr.s(auto_attribs=True)
class DomainSchemaOut:
    """
    Attributes:
        id (int): Id of the domain
        domain (Union[Unset, str]): No http:// or www. You can enter a path that must be found. Eg. example.com/path.
            Search result must then begin with your path to match.
        default_searchsettings_names (Union[Unset, List[SearchSettings]]): List of search settings that will be default
            for keywords on this domain.
        group_id (Union[Unset, int]): Id of the group the domain should belong to.
        display_name (Union[Unset, str]): <strong>Optional.</strong> If set this will display instead of the domain
            name. Automatically set for YouTube videos and channels.
        include_subdomains (Union[Unset, bool]): Include results from sub.domain.com.
        google_business_name_list (Union[Unset, List[str]]): For some local results Google does not include a link to
            the website. To make sure we can still find the domain on the search result page, please enter the exact name of
            the Google Business page here.
        twitter_handle (Union[Unset, str]): Enable ranking of your tweets on google.
        exact_match (Union[Unset, bool]): Only include results where the URL found is an exact match to what is entered
            in domain name
        share_of_voice_percentage (Union[Unset, bool]): Show Share of Voice in percentage for this domain
        paused (Union[Unset, bool]): Put updates on hold. This will free up the keywords the domain is using. Note that
            you can not un-pause the domain for 7 days.
    """

    id: int
    domain: Union[Unset, str] = UNSET
    default_searchsettings_names: Union[Unset, List[SearchSettings]] = UNSET
    group_id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    include_subdomains: Union[Unset, bool] = UNSET
    google_business_name_list: Union[Unset, List[str]] = UNSET
    twitter_handle: Union[Unset, str] = UNSET
    exact_match: Union[Unset, bool] = UNSET
    share_of_voice_percentage: Union[Unset, bool] = UNSET
    paused: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        domain = self.domain
        default_searchsettings_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_searchsettings_names, Unset):
            default_searchsettings_names = []
            for default_searchsettings_names_item_data in self.default_searchsettings_names:
                default_searchsettings_names_item = default_searchsettings_names_item_data.to_dict()

                default_searchsettings_names.append(default_searchsettings_names_item)




        group_id = self.group_id
        display_name = self.display_name
        include_subdomains = self.include_subdomains
        google_business_name_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.google_business_name_list, Unset):
            google_business_name_list = self.google_business_name_list




        twitter_handle = self.twitter_handle
        exact_match = self.exact_match
        share_of_voice_percentage = self.share_of_voice_percentage
        paused = self.paused

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if domain is not UNSET:
            field_dict["domain"] = domain
        if default_searchsettings_names is not UNSET:
            field_dict["default_searchsettings_names"] = default_searchsettings_names
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if include_subdomains is not UNSET:
            field_dict["include_subdomains"] = include_subdomains
        if google_business_name_list is not UNSET:
            field_dict["google_business_name_list"] = google_business_name_list
        if twitter_handle is not UNSET:
            field_dict["twitter_handle"] = twitter_handle
        if exact_match is not UNSET:
            field_dict["exact_match"] = exact_match
        if share_of_voice_percentage is not UNSET:
            field_dict["share_of_voice_percentage"] = share_of_voice_percentage
        if paused is not UNSET:
            field_dict["paused"] = paused

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        domain = d.pop("domain", UNSET)

        default_searchsettings_names = []
        _default_searchsettings_names = d.pop("default_searchsettings_names", UNSET)
        for default_searchsettings_names_item_data in (_default_searchsettings_names or []):
            default_searchsettings_names_item = SearchSettings.from_dict(default_searchsettings_names_item_data)



            default_searchsettings_names.append(default_searchsettings_names_item)


        group_id = d.pop("group_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        include_subdomains = d.pop("include_subdomains", UNSET)

        google_business_name_list = cast(List[str], d.pop("google_business_name_list", UNSET))


        twitter_handle = d.pop("twitter_handle", UNSET)

        exact_match = d.pop("exact_match", UNSET)

        share_of_voice_percentage = d.pop("share_of_voice_percentage", UNSET)

        paused = d.pop("paused", UNSET)

        domain_schema_out = cls(
            id=id,
            domain=domain,
            default_searchsettings_names=default_searchsettings_names,
            group_id=group_id,
            display_name=display_name,
            include_subdomains=include_subdomains,
            google_business_name_list=google_business_name_list,
            twitter_handle=twitter_handle,
            exact_match=exact_match,
            share_of_voice_percentage=share_of_voice_percentage,
            paused=paused,
        )

        domain_schema_out.additional_properties = d
        return domain_schema_out

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
