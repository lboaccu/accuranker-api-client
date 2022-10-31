
from typing import Any, Dict, List, Type, TypeVar, Union, NamedTuple

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountryLocale")

class CountryLocaleFields(NamedTuple):
    """
    Nested named tuple.
    """
    id = "search_locale.id"
    country_code = "search_locale.country_code"
    region = "search_locale.region"
    locale = "search_locale.locale"
    locale_short = "search_locale.locale_short"
    

@attr.s(auto_attribs=True)
class CountryLocale:
    """
    Attributes:
        id (Union[Unset, int]):
        country_code (Union[Unset, str]):
        region (Union[Unset, str]):
        locale (Union[Unset, str]):
        locale_short (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    country_code: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    locale_short: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        country_code = self.country_code
        region = self.region
        locale = self.locale
        locale_short = self.locale_short

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if region is not UNSET:
            field_dict["region"] = region
        if locale is not UNSET:
            field_dict["locale"] = locale
        if locale_short is not UNSET:
            field_dict["locale_short"] = locale_short

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        id = d.pop("id", UNSET)

        country_code = d.pop("country_code", UNSET)

        region = d.pop("region", UNSET)

        locale = d.pop("locale", UNSET)

        locale_short = d.pop("locale_short", UNSET)

        country_locale = cls(
            id=id,
            country_code=country_code,
            region=region,
            locale=locale,
            locale_short=locale_short,
        )

        country_locale.additional_properties = d
        return country_locale

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
