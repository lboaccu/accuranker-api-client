from typing import Any, Dict, List, Type, TypeVar, NamedTuple

import attr

from ..models.group_get import GroupGet

T = TypeVar("T", bound="Organization")

class OrganizationFields(NamedTuple):
    org_name = "org_name"
    id = "id"
    groups = "groups"

@attr.s(auto_attribs=True)
class Organization:
    """
    Attributes:
        org_name (str): The name of your organization/department. This will show up on reports.
        id (int): Id of the organization
        groups (List[GroupGet]): List of group that belongs to this organization
    """

    org_name: str
    id: int
    groups: List[GroupGet]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        org_name = self.org_name
        id = self.id
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()

            groups.append(groups_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "org_name": org_name,
            "id": id,
            "groups": groups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        org_name = d.pop("org_name")

        id = d.pop("id")

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in (_groups):
            groups_item = GroupGet.from_dict(groups_item_data)



            groups.append(groups_item)


        organization = cls(
            org_name=org_name,
            id=id,
            groups=groups,
        )

        organization.additional_properties = d
        return organization

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
