from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GroupOut")

@attr.s(auto_attribs=True)
class GroupOut:
    """
    Attributes:
        name (str): Name of the group
        organization (int): Id of the organization you want to the group to belong to.
        id (int): Id of the group
    """

    name: str
    organization: int
    id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization = self.organization
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "organization": organization,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization = d.pop("organization")

        id = d.pop("id")

        group_out = cls(
            name=name,
            organization=organization,
            id=id,
        )

        group_out.additional_properties = d
        return group_out

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
