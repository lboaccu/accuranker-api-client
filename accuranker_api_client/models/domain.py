import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast, NamedTuple

import attr
from dateutil.parser import isoparse


from ..models.client import Client
from ..models.competitor import Competitor
from ..models.search_volume_history import SearchVolumeHistory
from ..types import UNSET, Unset

T = TypeVar("T", bound="Domain")

class DomainFields(NamedTuple):
    id='id'
    last_scraped='last_scraped'
    group='group'
    domain='domain'
    display_name='display_name'
    created_at='created_at'
    google_business_name='google_business_name'
    google_business_name_list='google_business_name_list'
    competitors='competitors'
    history='history'
    additional_properties='additional_properties'

@attr.s(auto_attribs=True)
class Domain:
    """
    Attributes:
        id (Union[Unset, int]):
        last_scraped (Union[Unset, datetime.datetime]):
        group (Union[Unset, Client]):
        domain (Union[Unset, str]): No http:// or www. You can enter a path that must be found. Eg. example.com/path.
            Search result must then begin with your path to match.
        display_name (Union[Unset, None, str]): <strong>Optional.</strong> If set this will display instead of the
            domain name. Automatically set for YouTube videos and channels.
        created_at (Union[Unset, datetime.date]):
        google_business_name (Union[Unset, None, str]): For some local results Google does not include a link to the
            website. To make sure we can still find the domain on the search result page, please enter the exact name of the
            Google Business page here.
        google_business_name_list (Union[Unset, None, List[Optional[str]]]):
        competitors (Union[Unset, List[Competitor]]):
        history (Union[Unset, List[SearchVolumeHistory]]):
    """

    id: Union[Unset, int] = UNSET
    last_scraped: Union[Unset, datetime.datetime] = UNSET
    group: Union[Unset, Client] = UNSET
    domain: Union[Unset, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, datetime.date] = UNSET
    google_business_name: Union[Unset, None, str] = UNSET
    google_business_name_list: Union[Unset, None, List[Optional[str]]] = UNSET
    competitors: Union[Unset, List[Competitor]] = UNSET
    history: Union[Unset, List[SearchVolumeHistory]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        last_scraped: Union[Unset, str] = UNSET
        if not isinstance(self.last_scraped, Unset):
            last_scraped = self.last_scraped.isoformat()

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        domain = self.domain
        display_name = self.display_name
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        google_business_name = self.google_business_name
        google_business_name_list: Union[Unset, None, List[Optional[str]]] = UNSET
        if not isinstance(self.google_business_name_list, Unset):
            if self.google_business_name_list is None:
                google_business_name_list = None
            else:
                google_business_name_list = self.google_business_name_list




        competitors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = []
            for competitors_item_data in self.competitors:
                competitors_item = competitors_item_data.to_dict()

                competitors.append(competitors_item)




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
        if last_scraped is not UNSET:
            field_dict["last_scraped"] = last_scraped
        if group is not UNSET:
            field_dict["group"] = group
        if domain is not UNSET:
            field_dict["domain"] = domain
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if google_business_name is not UNSET:
            field_dict["google_business_name"] = google_business_name
        if google_business_name_list is not UNSET:
            field_dict["google_business_name_list"] = google_business_name_list
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _last_scraped = d.pop("last_scraped", UNSET)
        last_scraped: Union[Unset, datetime.datetime]
        if isinstance(_last_scraped,  Unset):
            last_scraped = UNSET
        else:
            last_scraped = isoparse(_last_scraped)




        _group = d.pop("group", UNSET)
        group: Union[Unset, Client]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = Client.from_dict(_group)




        domain = d.pop("domain", UNSET)

        display_name = d.pop("display_name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()




        google_business_name = d.pop("google_business_name", UNSET)

        google_business_name_list = cast(List[Optional[str]], d.pop("google_business_name_list", UNSET))


        competitors = []
        _competitors = d.pop("competitors", UNSET)
        for competitors_item_data in (_competitors or []):
            competitors_item = Competitor.from_dict(competitors_item_data)



            competitors.append(competitors_item)


        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in (_history or []):
            history_item = SearchVolumeHistory.from_dict(history_item_data)



            history.append(history_item)


        domain = cls(
            id=id,
            last_scraped=last_scraped,
            group=group,
            domain=domain,
            display_name=display_name,
            created_at=created_at,
            google_business_name=google_business_name,
            google_business_name_list=google_business_name_list,
            competitors=competitors,
            history=history,
        )

        domain.additional_properties = d
        return domain

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
