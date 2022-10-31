import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.competitor_google_business_name_list_item import CompetitorGoogleBusinessNameListItem
from ..models.search_volume_history import SearchVolumeHistory
from ..types import UNSET, Unset

T = TypeVar("T", bound="Competitor")

@attr.s(auto_attribs=True)
class Competitor:
    """
    Attributes:
        id (Union[Unset, int]):
        domain (Union[Unset, str]): No http:// or www. You can enter a path that must be found. Eg. example.com/path.
            Search result must then begin with your path to match.
        display_name (Union[Unset, str]): <strong>Optional.</strong> If set this will display instead of the domain
            name. Automatically set for YouTube videos and channels.
        google_business_name (Union[Unset, str]): For some local results Google does not include a link to the website.
            To make sure we can still find the domain on the search result page, please enter the exact name of the Google
            Business page here.
        google_business_name_list (Union[Unset, List[CompetitorGoogleBusinessNameListItem]]):
        created_at (Union[Unset, datetime.date]):
        history (Union[Unset, List[SearchVolumeHistory]]):
    """

    id: Union[Unset, int] = UNSET
    domain: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    google_business_name: Union[Unset, str] = UNSET
    google_business_name_list: Union[Unset, List[CompetitorGoogleBusinessNameListItem]] = UNSET
    created_at: Union[Unset, datetime.date] = UNSET
    history: Union[Unset, List[SearchVolumeHistory]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        domain = self.domain
        display_name = self.display_name
        google_business_name = self.google_business_name
        google_business_name_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.google_business_name_list, Unset):
            google_business_name_list = []
            for google_business_name_list_item_data in self.google_business_name_list:
                google_business_name_list_item = google_business_name_list_item_data.to_dict()

                google_business_name_list.append(google_business_name_list_item)




        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()

                history.append(history_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if google_business_name is not UNSET:
            field_dict["google_business_name"] = google_business_name
        if google_business_name_list is not UNSET:
            field_dict["google_business_name_list"] = google_business_name_list
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        domain = d.pop("domain", UNSET)

        display_name = d.pop("display_name", UNSET)

        google_business_name = d.pop("google_business_name", UNSET)

        google_business_name_list = []
        _google_business_name_list = d.pop("google_business_name_list", UNSET)
        for google_business_name_list_item_data in (_google_business_name_list or []):
            google_business_name_list_item = CompetitorGoogleBusinessNameListItem.from_dict(google_business_name_list_item_data)



            google_business_name_list.append(google_business_name_list_item)


        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()




        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in (_history or []):
            history_item = SearchVolumeHistory.from_dict(history_item_data)



            history.append(history_item)


        competitor = cls(
            id=id,
            domain=domain,
            display_name=display_name,
            google_business_name=google_business_name,
            google_business_name_list=google_business_name_list,
            created_at=created_at,
            history=history,
        )

        competitor.additional_properties = d
        return competitor

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
