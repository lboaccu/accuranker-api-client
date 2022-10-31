from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompetitorHistoryRankingMovement")

@attr.s(auto_attribs=True)
class CompetitorHistoryRankingMovement:
    """
    Attributes:
        winners (Union[Unset, int]):
        share_of_voice_winners (Union[Unset, int]):
        losers (Union[Unset, int]):
        share_of_voice_losers (Union[Unset, int]):
        no_movement (Union[Unset, int]):
        share_of_voice_no_movement (Union[Unset, int]):
    """

    winners: Union[Unset, int] = UNSET
    share_of_voice_winners: Union[Unset, int] = UNSET
    losers: Union[Unset, int] = UNSET
    share_of_voice_losers: Union[Unset, int] = UNSET
    no_movement: Union[Unset, int] = UNSET
    share_of_voice_no_movement: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        winners = self.winners
        share_of_voice_winners = self.share_of_voice_winners
        losers = self.losers
        share_of_voice_losers = self.share_of_voice_losers
        no_movement = self.no_movement
        share_of_voice_no_movement = self.share_of_voice_no_movement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if winners is not UNSET:
            field_dict["winners"] = winners
        if share_of_voice_winners is not UNSET:
            field_dict["share_of_voice_winners"] = share_of_voice_winners
        if losers is not UNSET:
            field_dict["losers"] = losers
        if share_of_voice_losers is not UNSET:
            field_dict["share_of_voice_losers"] = share_of_voice_losers
        if no_movement is not UNSET:
            field_dict["no_movement"] = no_movement
        if share_of_voice_no_movement is not UNSET:
            field_dict["share_of_voice_no_movement"] = share_of_voice_no_movement

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        winners = d.pop("winners", UNSET)

        share_of_voice_winners = d.pop("share_of_voice_winners", UNSET)

        losers = d.pop("losers", UNSET)

        share_of_voice_losers = d.pop("share_of_voice_losers", UNSET)

        no_movement = d.pop("no_movement", UNSET)

        share_of_voice_no_movement = d.pop("share_of_voice_no_movement", UNSET)

        competitor_history_ranking_movement = cls(
            winners=winners,
            share_of_voice_winners=share_of_voice_winners,
            losers=losers,
            share_of_voice_losers=share_of_voice_losers,
            no_movement=no_movement,
            share_of_voice_no_movement=share_of_voice_no_movement,
        )

        competitor_history_ranking_movement.additional_properties = d
        return competitor_history_ranking_movement

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
