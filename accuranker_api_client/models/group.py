from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Group")

@attr.s(auto_attribs=True)
class Group:
    """
    Attributes:
        name (str): Name of the group
        organization_id (int): Id of the organization you want to the group to belong to.
    """

    name: str
    organization_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "organization_id": organization_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_id = d.pop("organization_id")

        group = cls(
            name=name,
            organization_id=organization_id,
        )

        group.additional_properties = d
        return group

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
