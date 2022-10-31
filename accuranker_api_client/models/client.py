import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.organization import Organization
from ..types import UNSET, Unset

T = TypeVar("T", bound="Client")

@attr.s(auto_attribs=True)
class Client:
    """
    Attributes:
        id (Union[Unset, int]):
        account (Union[Unset, Organization]):
        name (Union[Unset, str]):
        created_at (Union[Unset, datetime.date]):
    """

    id: Union[Unset, int] = UNSET
    account: Union[Unset, Organization] = UNSET
    name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        name = self.name
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if account is not UNSET:
            field_dict["account"] = account
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _account = d.pop("account", UNSET)
        account: Union[Unset, Organization]
        if isinstance(_account,  Unset):
            account = UNSET
        else:
            account = Organization.from_dict(_account)




        name = d.pop("name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()




        client = cls(
            id=id,
            account=account,
            name=name,
            created_at=created_at,
        )

        client.additional_properties = d
        return client

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
