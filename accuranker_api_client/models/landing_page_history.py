import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LandingPageHistory")

@attr.s(auto_attribs=True)
class LandingPageHistory:
    """
    Attributes:
        date (Union[Unset, datetime.date]):
        average_rank (Union[Unset, float]):
        share_of_voice (Union[Unset, int]):
        share_of_voice_percentage (Union[Unset, float]):
        search_volume (Union[Unset, int]):
        keywords (Union[Unset, int]):
        average_ctr (Union[Unset, float]):
        average_ctr_max (Union[Unset, float]):
        estimated_visits (Union[Unset, int]):
        above_the_fold (Union[Unset, int]):
        informational_intent (Union[Unset, int]):
        transactional_intent (Union[Unset, int]):
        navigational_intent (Union[Unset, int]):
        commercial_intent (Union[Unset, int]):
    """

    date: Union[Unset, datetime.date] = UNSET
    average_rank: Union[Unset, float] = UNSET
    share_of_voice: Union[Unset, int] = UNSET
    share_of_voice_percentage: Union[Unset, float] = UNSET
    search_volume: Union[Unset, int] = UNSET
    keywords: Union[Unset, int] = UNSET
    average_ctr: Union[Unset, float] = UNSET
    average_ctr_max: Union[Unset, float] = UNSET
    estimated_visits: Union[Unset, int] = UNSET
    above_the_fold: Union[Unset, int] = UNSET
    informational_intent: Union[Unset, int] = UNSET
    transactional_intent: Union[Unset, int] = UNSET
    navigational_intent: Union[Unset, int] = UNSET
    commercial_intent: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        average_rank = self.average_rank
        share_of_voice = self.share_of_voice
        share_of_voice_percentage = self.share_of_voice_percentage
        search_volume = self.search_volume
        keywords = self.keywords
        average_ctr = self.average_ctr
        average_ctr_max = self.average_ctr_max
        estimated_visits = self.estimated_visits
        above_the_fold = self.above_the_fold
        informational_intent = self.informational_intent
        transactional_intent = self.transactional_intent
        navigational_intent = self.navigational_intent
        commercial_intent = self.commercial_intent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if average_rank is not UNSET:
            field_dict["average_rank"] = average_rank
        if share_of_voice is not UNSET:
            field_dict["share_of_voice"] = share_of_voice
        if share_of_voice_percentage is not UNSET:
            field_dict["share_of_voice_percentage"] = share_of_voice_percentage
        if search_volume is not UNSET:
            field_dict["search_volume"] = search_volume
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if average_ctr is not UNSET:
            field_dict["average_ctr"] = average_ctr
        if average_ctr_max is not UNSET:
            field_dict["average_ctr_max"] = average_ctr_max
        if estimated_visits is not UNSET:
            field_dict["estimated_visits"] = estimated_visits
        if above_the_fold is not UNSET:
            field_dict["above_the_fold"] = above_the_fold
        if informational_intent is not UNSET:
            field_dict["informational_intent"] = informational_intent
        if transactional_intent is not UNSET:
            field_dict["transactional_intent"] = transactional_intent
        if navigational_intent is not UNSET:
            field_dict["navigational_intent"] = navigational_intent
        if commercial_intent is not UNSET:
            field_dict["commercial_intent"] = commercial_intent

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        average_rank = d.pop("average_rank", UNSET)

        share_of_voice = d.pop("share_of_voice", UNSET)

        share_of_voice_percentage = d.pop("share_of_voice_percentage", UNSET)

        search_volume = d.pop("search_volume", UNSET)

        keywords = d.pop("keywords", UNSET)

        average_ctr = d.pop("average_ctr", UNSET)

        average_ctr_max = d.pop("average_ctr_max", UNSET)

        estimated_visits = d.pop("estimated_visits", UNSET)

        above_the_fold = d.pop("above_the_fold", UNSET)

        informational_intent = d.pop("informational_intent", UNSET)

        transactional_intent = d.pop("transactional_intent", UNSET)

        navigational_intent = d.pop("navigational_intent", UNSET)

        commercial_intent = d.pop("commercial_intent", UNSET)

        landing_page_history = cls(
            date=date,
            average_rank=average_rank,
            share_of_voice=share_of_voice,
            share_of_voice_percentage=share_of_voice_percentage,
            search_volume=search_volume,
            keywords=keywords,
            average_ctr=average_ctr,
            average_ctr_max=average_ctr_max,
            estimated_visits=estimated_visits,
            above_the_fold=above_the_fold,
            informational_intent=informational_intent,
            transactional_intent=transactional_intent,
            navigational_intent=navigational_intent,
            commercial_intent=commercial_intent,
        )

        landing_page_history.additional_properties = d
        return landing_page_history

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
