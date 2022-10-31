import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.competitor_history_ranking_distribution import CompetitorHistoryRankingDistribution
from ..models.competitor_history_ranking_movement import CompetitorHistoryRankingMovement
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompetitorHistory")

@attr.s(auto_attribs=True)
class CompetitorHistory:
    """
    Attributes:
        date (Union[Unset, datetime.date]):
        ranking_movement (Union[Unset, CompetitorHistoryRankingMovement]):
        ranking_distribution (Union[Unset, CompetitorHistoryRankingDistribution]):
        average_rank (Union[Unset, float]):
        share_of_voice (Union[Unset, int]):
        share_of_voice_percentage (Union[Unset, float]):
        average_ctr (Union[Unset, float]):
        average_ctr_max (Union[Unset, float]):
        estimated_visits (Union[Unset, int]):
    """

    date: Union[Unset, datetime.date] = UNSET
    ranking_movement: Union[Unset, CompetitorHistoryRankingMovement] = UNSET
    ranking_distribution: Union[Unset, CompetitorHistoryRankingDistribution] = UNSET
    average_rank: Union[Unset, float] = UNSET
    share_of_voice: Union[Unset, int] = UNSET
    share_of_voice_percentage: Union[Unset, float] = UNSET
    average_ctr: Union[Unset, float] = UNSET
    average_ctr_max: Union[Unset, float] = UNSET
    estimated_visits: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        ranking_movement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranking_movement, Unset):
            ranking_movement = self.ranking_movement.to_dict()

        ranking_distribution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranking_distribution, Unset):
            ranking_distribution = self.ranking_distribution.to_dict()

        average_rank = self.average_rank
        share_of_voice = self.share_of_voice
        share_of_voice_percentage = self.share_of_voice_percentage
        average_ctr = self.average_ctr
        average_ctr_max = self.average_ctr_max
        estimated_visits = self.estimated_visits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if ranking_movement is not UNSET:
            field_dict["ranking_movement"] = ranking_movement
        if ranking_distribution is not UNSET:
            field_dict["ranking_distribution"] = ranking_distribution
        if average_rank is not UNSET:
            field_dict["average_rank"] = average_rank
        if share_of_voice is not UNSET:
            field_dict["share_of_voice"] = share_of_voice
        if share_of_voice_percentage is not UNSET:
            field_dict["share_of_voice_percentage"] = share_of_voice_percentage
        if average_ctr is not UNSET:
            field_dict["average_ctr"] = average_ctr
        if average_ctr_max is not UNSET:
            field_dict["average_ctr_max"] = average_ctr_max
        if estimated_visits is not UNSET:
            field_dict["estimated_visits"] = estimated_visits

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        _ranking_movement = d.pop("ranking_movement", UNSET)
        ranking_movement: Union[Unset, CompetitorHistoryRankingMovement]
        if isinstance(_ranking_movement,  Unset):
            ranking_movement = UNSET
        else:
            ranking_movement = CompetitorHistoryRankingMovement.from_dict(_ranking_movement)




        _ranking_distribution = d.pop("ranking_distribution", UNSET)
        ranking_distribution: Union[Unset, CompetitorHistoryRankingDistribution]
        if isinstance(_ranking_distribution,  Unset):
            ranking_distribution = UNSET
        else:
            ranking_distribution = CompetitorHistoryRankingDistribution.from_dict(_ranking_distribution)




        average_rank = d.pop("average_rank", UNSET)

        share_of_voice = d.pop("share_of_voice", UNSET)

        share_of_voice_percentage = d.pop("share_of_voice_percentage", UNSET)

        average_ctr = d.pop("average_ctr", UNSET)

        average_ctr_max = d.pop("average_ctr_max", UNSET)

        estimated_visits = d.pop("estimated_visits", UNSET)

        competitor_history = cls(
            date=date,
            ranking_movement=ranking_movement,
            ranking_distribution=ranking_distribution,
            average_rank=average_rank,
            share_of_voice=share_of_voice,
            share_of_voice_percentage=share_of_voice_percentage,
            average_ctr=average_ctr,
            average_ctr_max=average_ctr_max,
            estimated_visits=estimated_visits,
        )

        competitor_history.additional_properties = d
        return competitor_history

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
