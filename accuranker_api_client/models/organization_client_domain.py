from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.organization import Organization

T = TypeVar("T", bound="OrganizationClientDomain")

@attr.s(auto_attribs=True)
class OrganizationClientDomain:
    """
    Attributes:
        organizations (List[Organization]): List of nested organization objects. Each organization contains multiple
            groups which contain multiple domains which contain multiple keywords
    """

    organizations: List[Organization]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()

            organizations.append(organizations_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "organizations": organizations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else dict(src_dict.copy())
        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in (_organizations):
            organizations_item = Organization.from_dict(organizations_item_data)



            organizations.append(organizations_item)


        organization_client_domain = cls(
            organizations=organizations,
        )

        organization_client_domain.additional_properties = d
        return organization_client_domain

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
