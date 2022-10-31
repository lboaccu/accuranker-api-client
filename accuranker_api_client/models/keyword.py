import datetime

from typing import Any, Dict, List, Type, TypeVar, Union, cast, NamedTuple

import attr
from dateutil.parser import isoparse

from ..models.country_locale import CountryLocale, CountryLocaleFields
from ..models.keyword_competitor_rank import KeywordCompetitorRank
from ..models.keyword_initial_rank import KeywordInitialRank
from ..models.keyword_rank import KeywordRank
from ..models.preferred_landing_page import PreferredLandingPage, PreferredLandingPageFields
from ..models.search_engine import SearchEngine, SearchEngineFields
from ..models.search_volume import SearchVolume
from ..types import UNSET, Unset

T = TypeVar("T", bound="Keyword")

class KeywordFields(NamedTuple):
    id = "id"
    keyword = "keyword"
    created_at = "created_at"
    search_locale = CountryLocaleFields
    search_location = "search_location"
    starred = "starred"
    tags = "tags"
    dynamic_tags = "dynamic_tags"
    search_engine = SearchEngineFields
    search_type = "search_type"
    preferred_landing_page = PreferredLandingPageFields
    search_volume = "search_volume"
    ranks = "ranks"
    initial_rank = "initial_rank"
    competitor_ranks = "competitor_ranks"
    

@attr.s(auto_attribs=True)
class Keyword:
    """
    Attributes:
        id (Union[Unset, int]):
        keyword (Union[Unset, str]):
        created_at (Union[Unset, datetime.date]):
        search_locale (Union[Unset, CountryLocale]):
        search_location (Union[Unset, str]):
        starred (Union[Unset, bool]):
        tags (Union[Unset, None, List[str]]):
        dynamic_tags (Union[Unset, None, List[str]]):
        search_engine (Union[Unset, SearchEngine]):
        search_type (Union[Unset, int]): 1 = Desktop and 2 = Mobile
        preferred_landing_page (Union[Unset, PreferredLandingPage]):
        search_volume (Union[Unset, SearchVolume]):
        ranks (Union[Unset, List[KeywordRank]]):
        initial_rank (Union[Unset, KeywordInitialRank]):
        competitor_ranks (Union[Unset, List[KeywordCompetitorRank]]):
    """

    id: Union[Unset, int] = UNSET
    keyword: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.date] = UNSET
    search_locale: Union[Unset, CountryLocale] = UNSET
    search_location: Union[Unset, str] = UNSET
    starred: Union[Unset, bool] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    dynamic_tags: Union[Unset, None, List[str]] = UNSET
    search_engine: Union[Unset, SearchEngine] = UNSET
    search_type: Union[Unset, int] = UNSET
    preferred_landing_page: Union[Unset, PreferredLandingPage] = UNSET
    search_volume: Union[Unset, SearchVolume] = UNSET
    ranks: Union[Unset, List[KeywordRank]] = UNSET
    initial_rank: Union[Unset, KeywordInitialRank] = UNSET
    competitor_ranks: Union[Unset, List[KeywordCompetitorRank]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        keyword = self.keyword
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        search_locale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_locale, Unset):
            search_locale = self.search_locale.to_dict()

        search_location = self.search_location
        starred = self.starred
        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags




        dynamic_tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.dynamic_tags, Unset):
            if self.dynamic_tags is None:
                dynamic_tags = None
            else:
                dynamic_tags = self.dynamic_tags




        search_engine: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_engine, Unset):
            search_engine = self.search_engine.to_dict()

        search_type = self.search_type
        preferred_landing_page: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preferred_landing_page, Unset):
            preferred_landing_page = self.preferred_landing_page.to_dict()

        search_volume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_volume, Unset):
            search_volume = self.search_volume.to_dict()

        ranks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = []
            for ranks_item_data in self.ranks:
                ranks_item = ranks_item_data.to_dict()

                ranks.append(ranks_item)




        initial_rank: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.initial_rank, Unset):
            initial_rank = self.initial_rank.to_dict()

        competitor_ranks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.competitor_ranks, Unset):
            competitor_ranks = []
            for competitor_ranks_item_data in self.competitor_ranks:
                competitor_ranks_item = competitor_ranks_item_data.to_dict()

                competitor_ranks.append(competitor_ranks_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if search_locale is not UNSET:
            field_dict["search_locale"] = search_locale
        if search_location is not UNSET:
            field_dict["search_location"] = search_location
        if starred is not UNSET:
            field_dict["starred"] = starred
        if tags is not UNSET:
            field_dict["tags"] = tags
        if dynamic_tags is not UNSET:
            field_dict["dynamic_tags"] = dynamic_tags
        if search_engine is not UNSET:
            field_dict["search_engine"] = search_engine
        if search_type is not UNSET:
            field_dict["search_type"] = search_type
        if preferred_landing_page is not UNSET:
            field_dict["preferred_landing_page"] = preferred_landing_page
        if search_volume is not UNSET:
            field_dict["search_volume"] = search_volume
        if ranks is not UNSET:
            field_dict["ranks"] = ranks
        if initial_rank is not UNSET:
            field_dict["initial_rank"] = initial_rank
        if competitor_ranks is not UNSET:
            field_dict["competitor_ranks"] = competitor_ranks

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        keyword = d.pop("keyword", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()




        _search_locale = d.pop("search_locale", UNSET)
        search_locale: Union[Unset, CountryLocale]
        if isinstance(_search_locale,  Unset):
            search_locale = UNSET
        else:
            search_locale = CountryLocale.from_dict(_search_locale)




        search_location = d.pop("search_location", UNSET)

        starred = d.pop("starred", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        dynamic_tags = cast(List[str], d.pop("dynamic_tags", UNSET))


        _search_engine = d.pop("search_engine", UNSET)
        search_engine: Union[Unset, SearchEngine]
        if isinstance(_search_engine,  Unset):
            search_engine = UNSET
        else:
            search_engine = SearchEngine.from_dict(_search_engine)




        search_type = d.pop("search_type", UNSET)

        _preferred_landing_page = d.pop("preferred_landing_page", UNSET)
        preferred_landing_page: Union[Unset, PreferredLandingPage]
        if isinstance(_preferred_landing_page,  Unset):
            preferred_landing_page = UNSET
        else:
            preferred_landing_page = PreferredLandingPage.from_dict(_preferred_landing_page)




        _search_volume = d.pop("search_volume", UNSET)
        search_volume: Union[Unset, SearchVolume]
        if isinstance(_search_volume,  Unset):
            search_volume = UNSET
        else:
            search_volume = SearchVolume.from_dict(_search_volume)




        ranks = []
        _ranks = d.pop("ranks", UNSET)
        for ranks_item_data in (_ranks or []):
            ranks_item = KeywordRank.from_dict(ranks_item_data)



            ranks.append(ranks_item)


        _initial_rank = d.pop("initial_rank", UNSET)
        initial_rank: Union[Unset, KeywordInitialRank]
        if isinstance(_initial_rank,  Unset):
            initial_rank = UNSET
        else:
            initial_rank = KeywordInitialRank.from_dict(_initial_rank)




        competitor_ranks = []
        _competitor_ranks = d.pop("competitor_ranks", UNSET)
        for competitor_ranks_item_data in (_competitor_ranks or []):
            competitor_ranks_item = KeywordCompetitorRank.from_dict(competitor_ranks_item_data)



            competitor_ranks.append(competitor_ranks_item)


        keyword = cls(
            id=id,
            keyword=keyword,
            created_at=created_at,
            search_locale=search_locale,
            search_location=search_location,
            starred=starred,
            tags=tags,
            dynamic_tags=dynamic_tags,
            search_engine=search_engine,
            search_type=search_type,
            preferred_landing_page=preferred_landing_page,
            search_volume=search_volume,
            ranks=ranks,
            initial_rank=initial_rank,
            competitor_ranks=competitor_ranks,
        )

        keyword.additional_properties = d
        return keyword

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
