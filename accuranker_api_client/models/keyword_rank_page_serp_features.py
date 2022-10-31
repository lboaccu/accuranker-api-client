from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordRankPageSerpFeatures")

@attr.s(auto_attribs=True)
class KeywordRankPageSerpFeatures:
    """
    Attributes:
        id (Union[Unset, int]):
        total (Union[Unset, int]):
        total_owned (Union[Unset, int]):
        ads_top (Union[Unset, bool]):
        ads_bottom (Union[Unset, bool]):
        autocorrect (Union[Unset, bool]):
        shopping (Union[Unset, bool]):
        maps_local_teaser (Union[Unset, bool]):
        maps_local (Union[Unset, bool]):
        related_questions (Union[Unset, bool]):
        carousel (Union[Unset, bool]):
        image_pack (Union[Unset, bool]):
        reviews (Union[Unset, bool]):
        tweets (Union[Unset, bool]):
        site_links (Union[Unset, bool]):
        feature_snippet (Union[Unset, bool]):
        knowledge_panel (Union[Unset, bool]):
        knowledge_cards (Union[Unset, bool]):
        video (Union[Unset, bool]):
        thumbnails (Union[Unset, bool]):
        breadcrumbs (Union[Unset, bool]):
        https (Union[Unset, bool]):
        direct_answer (Union[Unset, bool]):
        job_posting (Union[Unset, bool]):
        site_links_searchbox (Union[Unset, bool]):
        things_todo (Union[Unset, bool]):
        featured_video (Union[Unset, bool]):
        faq (Union[Unset, bool]):
        trips_popular (Union[Unset, bool]):
        podcasts (Union[Unset, bool]):
        related_searches_carousel (Union[Unset, bool]):
        most_popular_carousel (Union[Unset, bool]):
        refine_carousel (Union[Unset, bool]):
        results_about (Union[Unset, bool]):
        apps (Union[Unset, bool]):
        search_by_photos (Union[Unset, bool]):
        discover_more_places (Union[Unset, bool]):
        hotels_pack (Union[Unset, bool]):
        flights (Union[Unset, bool]):
        events (Union[Unset, bool]):
        popular_products (Union[Unset, bool]):
        maps_local_teaser_owned (Union[Unset, bool]):
        maps_local_owned (Union[Unset, bool]):
        related_questions_owned (Union[Unset, bool]):
        reviews_owned (Union[Unset, bool]):
        tweets_owned (Union[Unset, bool]):
        site_links_owned (Union[Unset, bool]):
        feature_snippet_owned (Union[Unset, bool]):
        knowledge_panel_owned (Union[Unset, bool]):
        video_owned (Union[Unset, bool]):
        thumbnails_owned (Union[Unset, bool]):
        breadcrumbs_owned (Union[Unset, bool]):
        https_owned (Union[Unset, bool]):
        site_links_searchbox_owned (Union[Unset, bool]):
        faq_owned (Union[Unset, bool]):
        featured_video_owned (Union[Unset, bool]):
        recipes_owned (Union[Unset, bool]):
        news_position (Union[Unset, int]):
        news_position_owned (Union[Unset, int]):
        video_carousel_position (Union[Unset, int]):
        video_carousel_position_owned (Union[Unset, int]):
        recipes_position (Union[Unset, int]):
        recipes_position_owned (Union[Unset, int]):
        research_product_position (Union[Unset, int]):
        research_product_position_owned (Union[Unset, int]):
        youtube_ads (Union[Unset, bool]):
        youtube_promoted_video (Union[Unset, bool]):
        youtube_promoted_video_owned (Union[Unset, bool]):
        youtube_related_searches (Union[Unset, bool]):
        youtube_related_to_your_search (Union[Unset, bool]):
        youtube_shelf_render (Union[Unset, bool]):
        youtube_related_movies (Union[Unset, bool]):
        youtube_secondary_search_container (Union[Unset, bool]):
        youtube_channel (Union[Unset, bool]):
        youtube_video (Union[Unset, bool]):
        youtube_show (Union[Unset, bool]):
        youtube_playlist (Union[Unset, bool]):
        youtube_movie (Union[Unset, bool]):
        youtube_live_stream (Union[Unset, bool]):
        youtube_radio (Union[Unset, bool]):
        youtube_channel_owned (Union[Unset, bool]):
        youtube_video_owned (Union[Unset, bool]):
        youtube_show_owned (Union[Unset, bool]):
        youtube_playlist_owned (Union[Unset, bool]):
        youtube_movie_owned (Union[Unset, bool]):
        youtube_live_stream_owned (Union[Unset, bool]):
        youtube_radio_owned (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    total_owned: Union[Unset, int] = UNSET
    ads_top: Union[Unset, bool] = UNSET
    ads_bottom: Union[Unset, bool] = UNSET
    autocorrect: Union[Unset, bool] = UNSET
    shopping: Union[Unset, bool] = UNSET
    maps_local_teaser: Union[Unset, bool] = UNSET
    maps_local: Union[Unset, bool] = UNSET
    related_questions: Union[Unset, bool] = UNSET
    carousel: Union[Unset, bool] = UNSET
    image_pack: Union[Unset, bool] = UNSET
    reviews: Union[Unset, bool] = UNSET
    tweets: Union[Unset, bool] = UNSET
    site_links: Union[Unset, bool] = UNSET
    feature_snippet: Union[Unset, bool] = UNSET
    knowledge_panel: Union[Unset, bool] = UNSET
    knowledge_cards: Union[Unset, bool] = UNSET
    video: Union[Unset, bool] = UNSET
    thumbnails: Union[Unset, bool] = UNSET
    breadcrumbs: Union[Unset, bool] = UNSET
    https: Union[Unset, bool] = UNSET
    direct_answer: Union[Unset, bool] = UNSET
    job_posting: Union[Unset, bool] = UNSET
    site_links_searchbox: Union[Unset, bool] = UNSET
    things_todo: Union[Unset, bool] = UNSET
    featured_video: Union[Unset, bool] = UNSET
    faq: Union[Unset, bool] = UNSET
    trips_popular: Union[Unset, bool] = UNSET
    podcasts: Union[Unset, bool] = UNSET
    related_searches_carousel: Union[Unset, bool] = UNSET
    most_popular_carousel: Union[Unset, bool] = UNSET
    refine_carousel: Union[Unset, bool] = UNSET
    results_about: Union[Unset, bool] = UNSET
    apps: Union[Unset, bool] = UNSET
    search_by_photos: Union[Unset, bool] = UNSET
    discover_more_places: Union[Unset, bool] = UNSET
    hotels_pack: Union[Unset, bool] = UNSET
    flights: Union[Unset, bool] = UNSET
    events: Union[Unset, bool] = UNSET
    popular_products: Union[Unset, bool] = UNSET
    maps_local_teaser_owned: Union[Unset, bool] = UNSET
    maps_local_owned: Union[Unset, bool] = UNSET
    related_questions_owned: Union[Unset, bool] = UNSET
    reviews_owned: Union[Unset, bool] = UNSET
    tweets_owned: Union[Unset, bool] = UNSET
    site_links_owned: Union[Unset, bool] = UNSET
    feature_snippet_owned: Union[Unset, bool] = UNSET
    knowledge_panel_owned: Union[Unset, bool] = UNSET
    video_owned: Union[Unset, bool] = UNSET
    thumbnails_owned: Union[Unset, bool] = UNSET
    breadcrumbs_owned: Union[Unset, bool] = UNSET
    https_owned: Union[Unset, bool] = UNSET
    site_links_searchbox_owned: Union[Unset, bool] = UNSET
    faq_owned: Union[Unset, bool] = UNSET
    featured_video_owned: Union[Unset, bool] = UNSET
    recipes_owned: Union[Unset, bool] = UNSET
    news_position: Union[Unset, int] = UNSET
    news_position_owned: Union[Unset, int] = UNSET
    video_carousel_position: Union[Unset, int] = UNSET
    video_carousel_position_owned: Union[Unset, int] = UNSET
    recipes_position: Union[Unset, int] = UNSET
    recipes_position_owned: Union[Unset, int] = UNSET
    research_product_position: Union[Unset, int] = UNSET
    research_product_position_owned: Union[Unset, int] = UNSET
    youtube_ads: Union[Unset, bool] = UNSET
    youtube_promoted_video: Union[Unset, bool] = UNSET
    youtube_promoted_video_owned: Union[Unset, bool] = UNSET
    youtube_related_searches: Union[Unset, bool] = UNSET
    youtube_related_to_your_search: Union[Unset, bool] = UNSET
    youtube_shelf_render: Union[Unset, bool] = UNSET
    youtube_related_movies: Union[Unset, bool] = UNSET
    youtube_secondary_search_container: Union[Unset, bool] = UNSET
    youtube_channel: Union[Unset, bool] = UNSET
    youtube_video: Union[Unset, bool] = UNSET
    youtube_show: Union[Unset, bool] = UNSET
    youtube_playlist: Union[Unset, bool] = UNSET
    youtube_movie: Union[Unset, bool] = UNSET
    youtube_live_stream: Union[Unset, bool] = UNSET
    youtube_radio: Union[Unset, bool] = UNSET
    youtube_channel_owned: Union[Unset, bool] = UNSET
    youtube_video_owned: Union[Unset, bool] = UNSET
    youtube_show_owned: Union[Unset, bool] = UNSET
    youtube_playlist_owned: Union[Unset, bool] = UNSET
    youtube_movie_owned: Union[Unset, bool] = UNSET
    youtube_live_stream_owned: Union[Unset, bool] = UNSET
    youtube_radio_owned: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        total = self.total
        total_owned = self.total_owned
        ads_top = self.ads_top
        ads_bottom = self.ads_bottom
        autocorrect = self.autocorrect
        shopping = self.shopping
        maps_local_teaser = self.maps_local_teaser
        maps_local = self.maps_local
        related_questions = self.related_questions
        carousel = self.carousel
        image_pack = self.image_pack
        reviews = self.reviews
        tweets = self.tweets
        site_links = self.site_links
        feature_snippet = self.feature_snippet
        knowledge_panel = self.knowledge_panel
        knowledge_cards = self.knowledge_cards
        video = self.video
        thumbnails = self.thumbnails
        breadcrumbs = self.breadcrumbs
        https = self.https
        direct_answer = self.direct_answer
        job_posting = self.job_posting
        site_links_searchbox = self.site_links_searchbox
        things_todo = self.things_todo
        featured_video = self.featured_video
        faq = self.faq
        trips_popular = self.trips_popular
        podcasts = self.podcasts
        related_searches_carousel = self.related_searches_carousel
        most_popular_carousel = self.most_popular_carousel
        refine_carousel = self.refine_carousel
        results_about = self.results_about
        apps = self.apps
        search_by_photos = self.search_by_photos
        discover_more_places = self.discover_more_places
        hotels_pack = self.hotels_pack
        flights = self.flights
        events = self.events
        popular_products = self.popular_products
        maps_local_teaser_owned = self.maps_local_teaser_owned
        maps_local_owned = self.maps_local_owned
        related_questions_owned = self.related_questions_owned
        reviews_owned = self.reviews_owned
        tweets_owned = self.tweets_owned
        site_links_owned = self.site_links_owned
        feature_snippet_owned = self.feature_snippet_owned
        knowledge_panel_owned = self.knowledge_panel_owned
        video_owned = self.video_owned
        thumbnails_owned = self.thumbnails_owned
        breadcrumbs_owned = self.breadcrumbs_owned
        https_owned = self.https_owned
        site_links_searchbox_owned = self.site_links_searchbox_owned
        faq_owned = self.faq_owned
        featured_video_owned = self.featured_video_owned
        recipes_owned = self.recipes_owned
        news_position = self.news_position
        news_position_owned = self.news_position_owned
        video_carousel_position = self.video_carousel_position
        video_carousel_position_owned = self.video_carousel_position_owned
        recipes_position = self.recipes_position
        recipes_position_owned = self.recipes_position_owned
        research_product_position = self.research_product_position
        research_product_position_owned = self.research_product_position_owned
        youtube_ads = self.youtube_ads
        youtube_promoted_video = self.youtube_promoted_video
        youtube_promoted_video_owned = self.youtube_promoted_video_owned
        youtube_related_searches = self.youtube_related_searches
        youtube_related_to_your_search = self.youtube_related_to_your_search
        youtube_shelf_render = self.youtube_shelf_render
        youtube_related_movies = self.youtube_related_movies
        youtube_secondary_search_container = self.youtube_secondary_search_container
        youtube_channel = self.youtube_channel
        youtube_video = self.youtube_video
        youtube_show = self.youtube_show
        youtube_playlist = self.youtube_playlist
        youtube_movie = self.youtube_movie
        youtube_live_stream = self.youtube_live_stream
        youtube_radio = self.youtube_radio
        youtube_channel_owned = self.youtube_channel_owned
        youtube_video_owned = self.youtube_video_owned
        youtube_show_owned = self.youtube_show_owned
        youtube_playlist_owned = self.youtube_playlist_owned
        youtube_movie_owned = self.youtube_movie_owned
        youtube_live_stream_owned = self.youtube_live_stream_owned
        youtube_radio_owned = self.youtube_radio_owned

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if total is not UNSET:
            field_dict["total"] = total
        if total_owned is not UNSET:
            field_dict["total_owned"] = total_owned
        if ads_top is not UNSET:
            field_dict["ads_top"] = ads_top
        if ads_bottom is not UNSET:
            field_dict["ads_bottom"] = ads_bottom
        if autocorrect is not UNSET:
            field_dict["autocorrect"] = autocorrect
        if shopping is not UNSET:
            field_dict["shopping"] = shopping
        if maps_local_teaser is not UNSET:
            field_dict["maps_local_teaser"] = maps_local_teaser
        if maps_local is not UNSET:
            field_dict["maps_local"] = maps_local
        if related_questions is not UNSET:
            field_dict["related_questions"] = related_questions
        if carousel is not UNSET:
            field_dict["carousel"] = carousel
        if image_pack is not UNSET:
            field_dict["image_pack"] = image_pack
        if reviews is not UNSET:
            field_dict["reviews"] = reviews
        if tweets is not UNSET:
            field_dict["tweets"] = tweets
        if site_links is not UNSET:
            field_dict["site_links"] = site_links
        if feature_snippet is not UNSET:
            field_dict["feature_snippet"] = feature_snippet
        if knowledge_panel is not UNSET:
            field_dict["knowledge_panel"] = knowledge_panel
        if knowledge_cards is not UNSET:
            field_dict["knowledge_cards"] = knowledge_cards
        if video is not UNSET:
            field_dict["video"] = video
        if thumbnails is not UNSET:
            field_dict["thumbnails"] = thumbnails
        if breadcrumbs is not UNSET:
            field_dict["breadcrumbs"] = breadcrumbs
        if https is not UNSET:
            field_dict["https"] = https
        if direct_answer is not UNSET:
            field_dict["direct_answer"] = direct_answer
        if job_posting is not UNSET:
            field_dict["job_posting"] = job_posting
        if site_links_searchbox is not UNSET:
            field_dict["site_links_searchbox"] = site_links_searchbox
        if things_todo is not UNSET:
            field_dict["things_todo"] = things_todo
        if featured_video is not UNSET:
            field_dict["featured_video"] = featured_video
        if faq is not UNSET:
            field_dict["faq"] = faq
        if trips_popular is not UNSET:
            field_dict["trips_popular"] = trips_popular
        if podcasts is not UNSET:
            field_dict["podcasts"] = podcasts
        if related_searches_carousel is not UNSET:
            field_dict["related_searches_carousel"] = related_searches_carousel
        if most_popular_carousel is not UNSET:
            field_dict["most_popular_carousel"] = most_popular_carousel
        if refine_carousel is not UNSET:
            field_dict["refine_carousel"] = refine_carousel
        if results_about is not UNSET:
            field_dict["results_about"] = results_about
        if apps is not UNSET:
            field_dict["apps"] = apps
        if search_by_photos is not UNSET:
            field_dict["search_by_photos"] = search_by_photos
        if discover_more_places is not UNSET:
            field_dict["discover_more_places"] = discover_more_places
        if hotels_pack is not UNSET:
            field_dict["hotels_pack"] = hotels_pack
        if flights is not UNSET:
            field_dict["flights"] = flights
        if events is not UNSET:
            field_dict["events"] = events
        if popular_products is not UNSET:
            field_dict["popular_products"] = popular_products
        if maps_local_teaser_owned is not UNSET:
            field_dict["maps_local_teaser_owned"] = maps_local_teaser_owned
        if maps_local_owned is not UNSET:
            field_dict["maps_local_owned"] = maps_local_owned
        if related_questions_owned is not UNSET:
            field_dict["related_questions_owned"] = related_questions_owned
        if reviews_owned is not UNSET:
            field_dict["reviews_owned"] = reviews_owned
        if tweets_owned is not UNSET:
            field_dict["tweets_owned"] = tweets_owned
        if site_links_owned is not UNSET:
            field_dict["site_links_owned"] = site_links_owned
        if feature_snippet_owned is not UNSET:
            field_dict["feature_snippet_owned"] = feature_snippet_owned
        if knowledge_panel_owned is not UNSET:
            field_dict["knowledge_panel_owned"] = knowledge_panel_owned
        if video_owned is not UNSET:
            field_dict["video_owned"] = video_owned
        if thumbnails_owned is not UNSET:
            field_dict["thumbnails_owned"] = thumbnails_owned
        if breadcrumbs_owned is not UNSET:
            field_dict["breadcrumbs_owned"] = breadcrumbs_owned
        if https_owned is not UNSET:
            field_dict["https_owned"] = https_owned
        if site_links_searchbox_owned is not UNSET:
            field_dict["site_links_searchbox_owned"] = site_links_searchbox_owned
        if faq_owned is not UNSET:
            field_dict["faq_owned"] = faq_owned
        if featured_video_owned is not UNSET:
            field_dict["featured_video_owned"] = featured_video_owned
        if recipes_owned is not UNSET:
            field_dict["recipes_owned"] = recipes_owned
        if news_position is not UNSET:
            field_dict["news_position"] = news_position
        if news_position_owned is not UNSET:
            field_dict["news_position_owned"] = news_position_owned
        if video_carousel_position is not UNSET:
            field_dict["video_carousel_position"] = video_carousel_position
        if video_carousel_position_owned is not UNSET:
            field_dict["video_carousel_position_owned"] = video_carousel_position_owned
        if recipes_position is not UNSET:
            field_dict["recipes_position"] = recipes_position
        if recipes_position_owned is not UNSET:
            field_dict["recipes_position_owned"] = recipes_position_owned
        if research_product_position is not UNSET:
            field_dict["research_product_position"] = research_product_position
        if research_product_position_owned is not UNSET:
            field_dict["research_product_position_owned"] = research_product_position_owned
        if youtube_ads is not UNSET:
            field_dict["youtube_ads"] = youtube_ads
        if youtube_promoted_video is not UNSET:
            field_dict["youtube_promoted_video"] = youtube_promoted_video
        if youtube_promoted_video_owned is not UNSET:
            field_dict["youtube_promoted_video_owned"] = youtube_promoted_video_owned
        if youtube_related_searches is not UNSET:
            field_dict["youtube_related_searches"] = youtube_related_searches
        if youtube_related_to_your_search is not UNSET:
            field_dict["youtube_related_to_your_search"] = youtube_related_to_your_search
        if youtube_shelf_render is not UNSET:
            field_dict["youtube_shelf_render"] = youtube_shelf_render
        if youtube_related_movies is not UNSET:
            field_dict["youtube_related_movies"] = youtube_related_movies
        if youtube_secondary_search_container is not UNSET:
            field_dict["youtube_secondary_search_container"] = youtube_secondary_search_container
        if youtube_channel is not UNSET:
            field_dict["youtube_channel"] = youtube_channel
        if youtube_video is not UNSET:
            field_dict["youtube_video"] = youtube_video
        if youtube_show is not UNSET:
            field_dict["youtube_show"] = youtube_show
        if youtube_playlist is not UNSET:
            field_dict["youtube_playlist"] = youtube_playlist
        if youtube_movie is not UNSET:
            field_dict["youtube_movie"] = youtube_movie
        if youtube_live_stream is not UNSET:
            field_dict["youtube_live_stream"] = youtube_live_stream
        if youtube_radio is not UNSET:
            field_dict["youtube_radio"] = youtube_radio
        if youtube_channel_owned is not UNSET:
            field_dict["youtube_channel_owned"] = youtube_channel_owned
        if youtube_video_owned is not UNSET:
            field_dict["youtube_video_owned"] = youtube_video_owned
        if youtube_show_owned is not UNSET:
            field_dict["youtube_show_owned"] = youtube_show_owned
        if youtube_playlist_owned is not UNSET:
            field_dict["youtube_playlist_owned"] = youtube_playlist_owned
        if youtube_movie_owned is not UNSET:
            field_dict["youtube_movie_owned"] = youtube_movie_owned
        if youtube_live_stream_owned is not UNSET:
            field_dict["youtube_live_stream_owned"] = youtube_live_stream_owned
        if youtube_radio_owned is not UNSET:
            field_dict["youtube_radio_owned"] = youtube_radio_owned

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        total = d.pop("total", UNSET)

        total_owned = d.pop("total_owned", UNSET)

        ads_top = d.pop("ads_top", UNSET)

        ads_bottom = d.pop("ads_bottom", UNSET)

        autocorrect = d.pop("autocorrect", UNSET)

        shopping = d.pop("shopping", UNSET)

        maps_local_teaser = d.pop("maps_local_teaser", UNSET)

        maps_local = d.pop("maps_local", UNSET)

        related_questions = d.pop("related_questions", UNSET)

        carousel = d.pop("carousel", UNSET)

        image_pack = d.pop("image_pack", UNSET)

        reviews = d.pop("reviews", UNSET)

        tweets = d.pop("tweets", UNSET)

        site_links = d.pop("site_links", UNSET)

        feature_snippet = d.pop("feature_snippet", UNSET)

        knowledge_panel = d.pop("knowledge_panel", UNSET)

        knowledge_cards = d.pop("knowledge_cards", UNSET)

        video = d.pop("video", UNSET)

        thumbnails = d.pop("thumbnails", UNSET)

        breadcrumbs = d.pop("breadcrumbs", UNSET)

        https = d.pop("https", UNSET)

        direct_answer = d.pop("direct_answer", UNSET)

        job_posting = d.pop("job_posting", UNSET)

        site_links_searchbox = d.pop("site_links_searchbox", UNSET)

        things_todo = d.pop("things_todo", UNSET)

        featured_video = d.pop("featured_video", UNSET)

        faq = d.pop("faq", UNSET)

        trips_popular = d.pop("trips_popular", UNSET)

        podcasts = d.pop("podcasts", UNSET)

        related_searches_carousel = d.pop("related_searches_carousel", UNSET)

        most_popular_carousel = d.pop("most_popular_carousel", UNSET)

        refine_carousel = d.pop("refine_carousel", UNSET)

        results_about = d.pop("results_about", UNSET)

        apps = d.pop("apps", UNSET)

        search_by_photos = d.pop("search_by_photos", UNSET)

        discover_more_places = d.pop("discover_more_places", UNSET)

        hotels_pack = d.pop("hotels_pack", UNSET)

        flights = d.pop("flights", UNSET)

        events = d.pop("events", UNSET)

        popular_products = d.pop("popular_products", UNSET)

        maps_local_teaser_owned = d.pop("maps_local_teaser_owned", UNSET)

        maps_local_owned = d.pop("maps_local_owned", UNSET)

        related_questions_owned = d.pop("related_questions_owned", UNSET)

        reviews_owned = d.pop("reviews_owned", UNSET)

        tweets_owned = d.pop("tweets_owned", UNSET)

        site_links_owned = d.pop("site_links_owned", UNSET)

        feature_snippet_owned = d.pop("feature_snippet_owned", UNSET)

        knowledge_panel_owned = d.pop("knowledge_panel_owned", UNSET)

        video_owned = d.pop("video_owned", UNSET)

        thumbnails_owned = d.pop("thumbnails_owned", UNSET)

        breadcrumbs_owned = d.pop("breadcrumbs_owned", UNSET)

        https_owned = d.pop("https_owned", UNSET)

        site_links_searchbox_owned = d.pop("site_links_searchbox_owned", UNSET)

        faq_owned = d.pop("faq_owned", UNSET)

        featured_video_owned = d.pop("featured_video_owned", UNSET)

        recipes_owned = d.pop("recipes_owned", UNSET)

        news_position = d.pop("news_position", UNSET)

        news_position_owned = d.pop("news_position_owned", UNSET)

        video_carousel_position = d.pop("video_carousel_position", UNSET)

        video_carousel_position_owned = d.pop("video_carousel_position_owned", UNSET)

        recipes_position = d.pop("recipes_position", UNSET)

        recipes_position_owned = d.pop("recipes_position_owned", UNSET)

        research_product_position = d.pop("research_product_position", UNSET)

        research_product_position_owned = d.pop("research_product_position_owned", UNSET)

        youtube_ads = d.pop("youtube_ads", UNSET)

        youtube_promoted_video = d.pop("youtube_promoted_video", UNSET)

        youtube_promoted_video_owned = d.pop("youtube_promoted_video_owned", UNSET)

        youtube_related_searches = d.pop("youtube_related_searches", UNSET)

        youtube_related_to_your_search = d.pop("youtube_related_to_your_search", UNSET)

        youtube_shelf_render = d.pop("youtube_shelf_render", UNSET)

        youtube_related_movies = d.pop("youtube_related_movies", UNSET)

        youtube_secondary_search_container = d.pop("youtube_secondary_search_container", UNSET)

        youtube_channel = d.pop("youtube_channel", UNSET)

        youtube_video = d.pop("youtube_video", UNSET)

        youtube_show = d.pop("youtube_show", UNSET)

        youtube_playlist = d.pop("youtube_playlist", UNSET)

        youtube_movie = d.pop("youtube_movie", UNSET)

        youtube_live_stream = d.pop("youtube_live_stream", UNSET)

        youtube_radio = d.pop("youtube_radio", UNSET)

        youtube_channel_owned = d.pop("youtube_channel_owned", UNSET)

        youtube_video_owned = d.pop("youtube_video_owned", UNSET)

        youtube_show_owned = d.pop("youtube_show_owned", UNSET)

        youtube_playlist_owned = d.pop("youtube_playlist_owned", UNSET)

        youtube_movie_owned = d.pop("youtube_movie_owned", UNSET)

        youtube_live_stream_owned = d.pop("youtube_live_stream_owned", UNSET)

        youtube_radio_owned = d.pop("youtube_radio_owned", UNSET)

        keyword_rank_page_serp_features = cls(
            id=id,
            total=total,
            total_owned=total_owned,
            ads_top=ads_top,
            ads_bottom=ads_bottom,
            autocorrect=autocorrect,
            shopping=shopping,
            maps_local_teaser=maps_local_teaser,
            maps_local=maps_local,
            related_questions=related_questions,
            carousel=carousel,
            image_pack=image_pack,
            reviews=reviews,
            tweets=tweets,
            site_links=site_links,
            feature_snippet=feature_snippet,
            knowledge_panel=knowledge_panel,
            knowledge_cards=knowledge_cards,
            video=video,
            thumbnails=thumbnails,
            breadcrumbs=breadcrumbs,
            https=https,
            direct_answer=direct_answer,
            job_posting=job_posting,
            site_links_searchbox=site_links_searchbox,
            things_todo=things_todo,
            featured_video=featured_video,
            faq=faq,
            trips_popular=trips_popular,
            podcasts=podcasts,
            related_searches_carousel=related_searches_carousel,
            most_popular_carousel=most_popular_carousel,
            refine_carousel=refine_carousel,
            results_about=results_about,
            apps=apps,
            search_by_photos=search_by_photos,
            discover_more_places=discover_more_places,
            hotels_pack=hotels_pack,
            flights=flights,
            events=events,
            popular_products=popular_products,
            maps_local_teaser_owned=maps_local_teaser_owned,
            maps_local_owned=maps_local_owned,
            related_questions_owned=related_questions_owned,
            reviews_owned=reviews_owned,
            tweets_owned=tweets_owned,
            site_links_owned=site_links_owned,
            feature_snippet_owned=feature_snippet_owned,
            knowledge_panel_owned=knowledge_panel_owned,
            video_owned=video_owned,
            thumbnails_owned=thumbnails_owned,
            breadcrumbs_owned=breadcrumbs_owned,
            https_owned=https_owned,
            site_links_searchbox_owned=site_links_searchbox_owned,
            faq_owned=faq_owned,
            featured_video_owned=featured_video_owned,
            recipes_owned=recipes_owned,
            news_position=news_position,
            news_position_owned=news_position_owned,
            video_carousel_position=video_carousel_position,
            video_carousel_position_owned=video_carousel_position_owned,
            recipes_position=recipes_position,
            recipes_position_owned=recipes_position_owned,
            research_product_position=research_product_position,
            research_product_position_owned=research_product_position_owned,
            youtube_ads=youtube_ads,
            youtube_promoted_video=youtube_promoted_video,
            youtube_promoted_video_owned=youtube_promoted_video_owned,
            youtube_related_searches=youtube_related_searches,
            youtube_related_to_your_search=youtube_related_to_your_search,
            youtube_shelf_render=youtube_shelf_render,
            youtube_related_movies=youtube_related_movies,
            youtube_secondary_search_container=youtube_secondary_search_container,
            youtube_channel=youtube_channel,
            youtube_video=youtube_video,
            youtube_show=youtube_show,
            youtube_playlist=youtube_playlist,
            youtube_movie=youtube_movie,
            youtube_live_stream=youtube_live_stream,
            youtube_radio=youtube_radio,
            youtube_channel_owned=youtube_channel_owned,
            youtube_video_owned=youtube_video_owned,
            youtube_show_owned=youtube_show_owned,
            youtube_playlist_owned=youtube_playlist_owned,
            youtube_movie_owned=youtube_movie_owned,
            youtube_live_stream_owned=youtube_live_stream_owned,
            youtube_radio_owned=youtube_radio_owned,
        )

        keyword_rank_page_serp_features.additional_properties = d
        return keyword_rank_page_serp_features

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
