from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.domain_get import DomainGet

T = TypeVar("T", bound="GroupGet")

@attr.s(auto_attribs=True)
class GroupGet:
    """
    Attributes:
        group_name (str): Name of the group
        id (int): Id of the group
        domains (List[DomainGet]): List of domains that belongs to the group.
    """

    group_name: str
    id: int
    domains: List[DomainGet]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name
        id = self.id
        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()

            domains.append(domains_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "group_name": group_name,
            "id": id,
            "domains": domains,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        group_name = d.pop("group_name")

        id = d.pop("id")

        domains = []
        _domains = d.pop("domains")
        for domains_item_data in (_domains):
            domains_item = DomainGet.from_dict(domains_item_data)



            domains.append(domains_item)


        group_get = cls(
            group_name=group_name,
            id=id,
            domains=domains,
        )

        group_get.additional_properties = d
        return group_get

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
