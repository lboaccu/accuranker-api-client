from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainHistoryRankingDistribution")

@attr.s(auto_attribs=True)
class DomainHistoryRankingDistribution:
    """
    Attributes:
        keywords_0_3 (Union[Unset, int]):
        keywords_4_10 (Union[Unset, int]):
        keywords_11_20 (Union[Unset, int]):
        keywords_21_50 (Union[Unset, int]):
        keywords_above_50 (Union[Unset, int]):
        keywords_unranked (Union[Unset, int]):
        keywords_total (Union[Unset, int]):
    """

    keywords_0_3: Union[Unset, int] = UNSET
    keywords_4_10: Union[Unset, int] = UNSET
    keywords_11_20: Union[Unset, int] = UNSET
    keywords_21_50: Union[Unset, int] = UNSET
    keywords_above_50: Union[Unset, int] = UNSET
    keywords_unranked: Union[Unset, int] = UNSET
    keywords_total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        keywords_0_3 = self.keywords_0_3
        keywords_4_10 = self.keywords_4_10
        keywords_11_20 = self.keywords_11_20
        keywords_21_50 = self.keywords_21_50
        keywords_above_50 = self.keywords_above_50
        keywords_unranked = self.keywords_unranked
        keywords_total = self.keywords_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if keywords_0_3 is not UNSET:
            field_dict["keywords_0_3"] = keywords_0_3
        if keywords_4_10 is not UNSET:
            field_dict["keywords_4_10"] = keywords_4_10
        if keywords_11_20 is not UNSET:
            field_dict["keywords_11_20"] = keywords_11_20
        if keywords_21_50 is not UNSET:
            field_dict["keywords_21_50"] = keywords_21_50
        if keywords_above_50 is not UNSET:
            field_dict["keywords_above_50"] = keywords_above_50
        if keywords_unranked is not UNSET:
            field_dict["keywords_unranked"] = keywords_unranked
        if keywords_total is not UNSET:
            field_dict["keywords_total"] = keywords_total

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keywords_0_3 = d.pop("keywords_0_3", UNSET)

        keywords_4_10 = d.pop("keywords_4_10", UNSET)

        keywords_11_20 = d.pop("keywords_11_20", UNSET)

        keywords_21_50 = d.pop("keywords_21_50", UNSET)

        keywords_above_50 = d.pop("keywords_above_50", UNSET)

        keywords_unranked = d.pop("keywords_unranked", UNSET)

        keywords_total = d.pop("keywords_total", UNSET)

        domain_history_ranking_distribution = cls(
            keywords_0_3=keywords_0_3,
            keywords_4_10=keywords_4_10,
            keywords_11_20=keywords_11_20,
            keywords_21_50=keywords_21_50,
            keywords_above_50=keywords_above_50,
            keywords_unranked=keywords_unranked,
            keywords_total=keywords_total,
        )

        domain_history_ranking_distribution.additional_properties = d
        return domain_history_ranking_distribution

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
