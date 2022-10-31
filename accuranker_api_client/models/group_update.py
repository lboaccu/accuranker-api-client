from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupUpdate")

@attr.s(auto_attribs=True)
class GroupUpdate:
    """
    Attributes:
        group_name (Union[Unset, str]): Name of the group
        organization_id (Union[Unset, int]): Id of the organization you want to move the group to.
    """

    group_name: Union[Unset, str] = UNSET
    organization_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name
        organization_id = self.organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if organization_id is not UNSET:
            field_dict["organization.id"] = organization_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_name = d.pop("group_name", UNSET)

        organization_id = d.pop("organization.id", UNSET)

        group_update = cls(
            group_name=group_name,
            organization_id=organization_id,
        )

        group_update.additional_properties = d
        return group_update

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
