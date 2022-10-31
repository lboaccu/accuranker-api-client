
from typing import Any, Dict, List, Type, TypeVar, Union, NamedTuple

import attr

from ..models.search_volume_history import SearchVolumeHistory, SearchVolumeHistoryFields
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchVolume")

class SearchVolumeFields(NamedTuple):
    id = "id"
    search_volume = "search_volume"
    avg_cost_per_click = "avg_cost_per_click"
    competition = "competition"
    history = SearchVolumeHistoryFields
    

@attr.s(auto_attribs=True)
class SearchVolume:
    """
    Attributes:
        id (Union[Unset, int]):
        search_volume (Union[Unset, int]):
        avg_cost_per_click (Union[Unset, None, float]):
        competition (Union[Unset, None, float]):
        history (Union[Unset, List[SearchVolumeHistory]]):
    """

    id: Union[Unset, int] = UNSET
    search_volume: Union[Unset, int] = UNSET
    avg_cost_per_click: Union[Unset, None, float] = UNSET
    competition: Union[Unset, None, float] = UNSET
    history: Union[Unset, List[SearchVolumeHistory]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        search_volume = self.search_volume
        avg_cost_per_click = self.avg_cost_per_click
        competition = self.competition
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
        if search_volume is not UNSET:
            field_dict["search_volume"] = search_volume
        if avg_cost_per_click is not UNSET:
            field_dict["avg_cost_per_click"] = avg_cost_per_click
        if competition is not UNSET:
            field_dict["competition"] = competition
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        search_volume = d.pop("search_volume", UNSET)

        avg_cost_per_click = d.pop("avg_cost_per_click", UNSET)

        competition = d.pop("competition", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in (_history or []):
            history_item = SearchVolumeHistory.from_dict(history_item_data)



            history.append(history_item)


        search_volume = cls(
            id=id,
            search_volume=search_volume,
            avg_cost_per_click=avg_cost_per_click,
            competition=competition,
            history=history,
        )

        search_volume.additional_properties = d
        return search_volume

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
