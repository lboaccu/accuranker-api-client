from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DomainGet")

@attr.s(auto_attribs=True)
class DomainGet:
    """
    Attributes:
        domain (str): Domain that is looked for when searching for keywords, eg. 'bbc.co.uk'
        display_name (str): Domain name as it is displayed in the app. Usually defined by the user.
        id (int): Id of the domain
    """

    domain: str
    display_name: str
    id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain
        display_name = self.display_name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "domain": domain,
            "display_name": display_name,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        domain = d.pop("domain")

        display_name = d.pop("display_name")

        id = d.pop("id")

        domain_get = cls(
            domain=domain,
            display_name=display_name,
            id=id,
        )

        domain_get.additional_properties = d
        return domain_get

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
