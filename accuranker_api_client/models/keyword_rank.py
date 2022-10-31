import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.keyword_rank_landing_page import KeywordRankLandingPage
from ..models.keyword_rank_page_serp_features import KeywordRankPageSerpFeatures
from ..models.keyword_rank_search_intent_item import KeywordRankSearchIntentItem
from ..models.keyword_rank_title_description import KeywordRankTitleDescription
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordRank")

@attr.s(auto_attribs=True)
class KeywordRank:
    """
    Attributes:
        id (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        rank (Union[Unset, int]):
        share_of_voice (Union[Unset, int]):
        share_of_voice_percentage (Union[Unset, float]):
        estimated_visits (Union[Unset, int]):
        ctr (Union[Unset, float]):
        ctr_max (Union[Unset, float]):
        search_intent (Union[Unset, List[KeywordRankSearchIntentItem]]):
        highest_ranking_page (Union[Unset, str]):
        landing_page (Union[Unset, KeywordRankLandingPage]):
        title_description (Union[Unset, KeywordRankTitleDescription]):
        extra_ranks (Union[Unset, List[List[str]]]):
        above_the_fold (Union[Unset, bool]):
        browser_position_x1 (Union[Unset, int]):
        browser_position_y1 (Union[Unset, int]):
        browser_position_x2 (Union[Unset, int]):
        browser_position_y2 (Union[Unset, int]):
        page_serp_features (Union[Unset, KeywordRankPageSerpFeatures]):
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    rank: Union[Unset, int] = UNSET
    share_of_voice: Union[Unset, int] = UNSET
    share_of_voice_percentage: Union[Unset, float] = UNSET
    estimated_visits: Union[Unset, int] = UNSET
    ctr: Union[Unset, float] = UNSET
    ctr_max: Union[Unset, float] = UNSET
    search_intent: Union[Unset, List[KeywordRankSearchIntentItem]] = UNSET
    highest_ranking_page: Union[Unset, str] = UNSET
    landing_page: Union[Unset, KeywordRankLandingPage] = UNSET
    title_description: Union[Unset, KeywordRankTitleDescription] = UNSET
    extra_ranks: Union[Unset, List[List[str]]] = UNSET
    above_the_fold: Union[Unset, bool] = UNSET
    browser_position_x1: Union[Unset, int] = UNSET
    browser_position_y1: Union[Unset, int] = UNSET
    browser_position_x2: Union[Unset, int] = UNSET
    browser_position_y2: Union[Unset, int] = UNSET
    page_serp_features: Union[Unset, KeywordRankPageSerpFeatures] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        rank = self.rank
        share_of_voice = self.share_of_voice
        share_of_voice_percentage = self.share_of_voice_percentage
        estimated_visits = self.estimated_visits
        ctr = self.ctr
        ctr_max = self.ctr_max
        search_intent: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.search_intent, Unset):
            search_intent = []
            for search_intent_item_data in self.search_intent:
                search_intent_item = search_intent_item_data.to_dict()

                search_intent.append(search_intent_item)




        highest_ranking_page = self.highest_ranking_page
        landing_page: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.landing_page, Unset):
            landing_page = self.landing_page.to_dict()

        title_description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title_description, Unset):
            title_description = self.title_description.to_dict()

        extra_ranks: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.extra_ranks, Unset):
            extra_ranks = []
            for extra_ranks_item_data in self.extra_ranks:
                extra_ranks_item = extra_ranks_item_data




                extra_ranks.append(extra_ranks_item)




        above_the_fold = self.above_the_fold
        browser_position_x1 = self.browser_position_x1
        browser_position_y1 = self.browser_position_y1
        browser_position_x2 = self.browser_position_x2
        browser_position_y2 = self.browser_position_y2
        page_serp_features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.page_serp_features, Unset):
            page_serp_features = self.page_serp_features.to_dict()


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
        if estimated_visits is not UNSET:
            field_dict["estimated_visits"] = estimated_visits
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if ctr_max is not UNSET:
            field_dict["ctr_max"] = ctr_max
        if search_intent is not UNSET:
            field_dict["search_intent"] = search_intent
        if highest_ranking_page is not UNSET:
            field_dict["highest_ranking_page"] = highest_ranking_page
        if landing_page is not UNSET:
            field_dict["landing_page"] = landing_page
        if title_description is not UNSET:
            field_dict["title_description"] = title_description
        if extra_ranks is not UNSET:
            field_dict["extra_ranks"] = extra_ranks
        if above_the_fold is not UNSET:
            field_dict["above_the_fold"] = above_the_fold
        if browser_position_x1 is not UNSET:
            field_dict["browser_position_x1"] = browser_position_x1
        if browser_position_y1 is not UNSET:
            field_dict["browser_position_y1"] = browser_position_y1
        if browser_position_x2 is not UNSET:
            field_dict["browser_position_x2"] = browser_position_x2
        if browser_position_y2 is not UNSET:
            field_dict["browser_position_y2"] = browser_position_y2
        if page_serp_features is not UNSET:
            field_dict["page_serp_features"] = page_serp_features

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

        estimated_visits = d.pop("estimated_visits", UNSET)

        ctr = d.pop("ctr", UNSET)

        ctr_max = d.pop("ctr_max", UNSET)

        search_intent = []
        _search_intent = d.pop("search_intent", UNSET)
        for search_intent_item_data in (_search_intent or []):
            search_intent_item = KeywordRankSearchIntentItem.from_dict(search_intent_item_data)



            search_intent.append(search_intent_item)


        highest_ranking_page = d.pop("highest_ranking_page", UNSET)

        _landing_page = d.pop("landing_page", UNSET)
        landing_page: Union[Unset, KeywordRankLandingPage]
        if isinstance(_landing_page,  Unset):
            landing_page = UNSET
        else:
            landing_page = KeywordRankLandingPage.from_dict(_landing_page)




        _title_description = d.pop("title_description", UNSET)
        title_description: Union[Unset, KeywordRankTitleDescription]
        if isinstance(_title_description,  Unset):
            title_description = UNSET
        else:
            title_description = KeywordRankTitleDescription.from_dict(_title_description)




        extra_ranks = []
        _extra_ranks = d.pop("extra_ranks", UNSET)
        for extra_ranks_item_data in (_extra_ranks or []):
            extra_ranks_item = cast(List[str], extra_ranks_item_data)

            extra_ranks.append(extra_ranks_item)


        above_the_fold = d.pop("above_the_fold", UNSET)

        browser_position_x1 = d.pop("browser_position_x1", UNSET)

        browser_position_y1 = d.pop("browser_position_y1", UNSET)

        browser_position_x2 = d.pop("browser_position_x2", UNSET)

        browser_position_y2 = d.pop("browser_position_y2", UNSET)

        _page_serp_features = d.pop("page_serp_features", UNSET)
        page_serp_features: Union[Unset, KeywordRankPageSerpFeatures]
        if isinstance(_page_serp_features,  Unset):
            page_serp_features = UNSET
        else:
            page_serp_features = KeywordRankPageSerpFeatures.from_dict(_page_serp_features)




        keyword_rank = cls(
            id=id,
            created_at=created_at,
            rank=rank,
            share_of_voice=share_of_voice,
            share_of_voice_percentage=share_of_voice_percentage,
            estimated_visits=estimated_visits,
            ctr=ctr,
            ctr_max=ctr_max,
            search_intent=search_intent,
            highest_ranking_page=highest_ranking_page,
            landing_page=landing_page,
            title_description=title_description,
            extra_ranks=extra_ranks,
            above_the_fold=above_the_fold,
            browser_position_x1=browser_position_x1,
            browser_position_y1=browser_position_y1,
            browser_position_x2=browser_position_x2,
            browser_position_y2=browser_position_y2,
            page_serp_features=page_serp_features,
        )

        keyword_rank.additional_properties = d
        return keyword_rank

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
