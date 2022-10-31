import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.keyword_competitor_rank_competitor import KeywordCompetitorRankCompetitor
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordCompetitorRank")

@attr.s(auto_attribs=True)
class KeywordCompetitorRank:
    """
    Attributes:
        id (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        rank (Union[Unset, int]):
        share_of_voice (Union[Unset, int]):
        share_of_voice_percentage (Union[Unset, float]):
        competitor (Union[Unset, KeywordCompetitorRankCompetitor]):
        highest_ranking_page (Union[Unset, str]):
        estimated_visits (Union[Unset, int]):
        ctr (Union[Unset, float]):
        ctr_max (Union[Unset, float]):
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    rank: Union[Unset, int] = UNSET
    share_of_voice: Union[Unset, int] = UNSET
    share_of_voice_percentage: Union[Unset, float] = UNSET
    competitor: Union[Unset, KeywordCompetitorRankCompetitor] = UNSET
    highest_ranking_page: Union[Unset, str] = UNSET
    estimated_visits: Union[Unset, int] = UNSET
    ctr: Union[Unset, float] = UNSET
    ctr_max: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        rank = self.rank
        share_of_voice = self.share_of_voice
        share_of_voice_percentage = self.share_of_voice_percentage
        competitor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.competitor, Unset):
            competitor = self.competitor.to_dict()

        highest_ranking_page = self.highest_ranking_page
        estimated_visits = self.estimated_visits
        ctr = self.ctr
        ctr_max = self.ctr_max

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if rank is not UNSET:
            field_dict["rank"] = rank
        if share_of_voice is not UNSET:
            field_dict["share_of_voice"] = share_of_voice
        if share_of_voice_percentage is not UNSET:
            field_dict["share_of_voice_percentage"] = share_of_voice_percentage
        if competitor is not UNSET:
            field_dict["competitor"] = competitor
        if highest_ranking_page is not UNSET:
            field_dict["highest_ranking_page"] = highest_ranking_page
        if estimated_visits is not UNSET:
            field_dict["estimated_visits"] = estimated_visits
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if ctr_max is not UNSET:
            field_dict["ctr_max"] = ctr_max

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        rank = d.pop("rank", UNSET)

        share_of_voice = d.pop("share_of_voice", UNSET)

        share_of_voice_percentage = d.pop("share_of_voice_percentage", UNSET)

        _competitor = d.pop("competitor", UNSET)
        competitor: Union[Unset, KeywordCompetitorRankCompetitor]
        if isinstance(_competitor,  Unset):
            competitor = UNSET
        else:
            competitor = KeywordCompetitorRankCompetitor.from_dict(_competitor)




        highest_ranking_page = d.pop("highest_ranking_page", UNSET)

        estimated_visits = d.pop("estimated_visits", UNSET)

        ctr = d.pop("ctr", UNSET)

        ctr_max = d.pop("ctr_max", UNSET)

        keyword_competitor_rank = cls(
            id=id,
            created_at=created_at,
            rank=rank,
            share_of_voice=share_of_voice,
            share_of_voice_percentage=share_of_voice_percentage,
            competitor=competitor,
            highest_ranking_page=highest_ranking_page,
            estimated_visits=estimated_visits,
            ctr=ctr,
            ctr_max=ctr_max,
        )

        keyword_competitor_rank.additional_properties = d
        return keyword_competitor_rank

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
