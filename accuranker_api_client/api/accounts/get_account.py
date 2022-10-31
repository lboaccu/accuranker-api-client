from typing import Any, Dict, Optional, Union, cast, List

import httpx

from ...client import Client
from ...models.organization import Organization, OrganizationFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[OrganizationFields]] = UNSET,

) -> Dict[str, Any]:
    url = "{}/accounts/{id}/".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["fields"] = fields



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Organization]]:
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())



        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Organization]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[OrganizationFields]] = UNSET,

) -> Response[Union[Any, Organization]]:
    """
    Args:
        id (int):
        fields (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Organization]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
fields=fields,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[OrganizationFields]] = UNSET,

) -> Optional[Union[Any, Organization]]:
    """
    Args:
        id (int):
        fields (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Organization]]
    """


    return sync_detailed(
        id=id,
client=client,
fields=fields,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[OrganizationFields]] = UNSET,

) -> Response[Union[Any, Organization]]:
    """
    Args:
        id (int):
        fields (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Organization]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
fields=fields,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[OrganizationFields]] = UNSET,

) -> Optional[Union[Any, Organization]]:
    """
    Args:
        id (int):
        fields (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, Organization]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
fields=fields,

    )).parsed

