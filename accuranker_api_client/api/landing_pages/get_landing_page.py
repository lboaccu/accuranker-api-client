from typing import Any, Dict, Optional, Union, cast, List

import httpx

from ...client import Client
from ...models.landing_page_serializer_schema import LandingPageSerializerSchema, LandingPageSerializerSchemaFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    domain_pk: int,
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[LandingPageSerializerSchemaFields]] = UNSET,
    period_from: Union[Unset, None, str] = UNSET,
    period_to: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, int] = UNSET,

) -> Dict[str, Any]:
    url = "{}/domains/{domain_pk}/landing_pages/{id}/".format(
        client.base_url,domain_pk=domain_pk,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()





    params: Dict[str, Any] = {}
    params["fields"] = fields


    params["period_from"] = period_from


    params["period_to"] = period_to


    params["filter"] = filter_



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}






    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, LandingPageSerializerSchema]]:
    if response.status_code == 200:
        response_200 = LandingPageSerializerSchema.from_dict(response.json())



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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, LandingPageSerializerSchema]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    domain_pk: int,
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[LandingPageSerializerSchemaFields]] = UNSET,
    period_from: Union[Unset, None, str] = UNSET,
    period_to: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, int] = UNSET,

) -> Response[Union[Any, LandingPageSerializerSchema]]:
    """
    Args:
        domain_pk (int):
        id (int):
        fields (Union[Unset, None, str]):
        period_from (Union[Unset, None, str]):
        period_to (Union[Unset, None, str]):
        filter_ (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, LandingPageSerializerSchema]]
    """


    kwargs = _get_kwargs(
        domain_pk=domain_pk,
id=id,
client=client,
fields=fields,
period_from=period_from,
period_to=period_to,
filter_=filter_,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    domain_pk: int,
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[LandingPageSerializerSchemaFields]] = UNSET,
    period_from: Union[Unset, None, str] = UNSET,
    period_to: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, int] = UNSET,

) -> Optional[Union[Any, LandingPageSerializerSchema]]:
    """
    Args:
        domain_pk (int):
        id (int):
        fields (Union[Unset, None, str]):
        period_from (Union[Unset, None, str]):
        period_to (Union[Unset, None, str]):
        filter_ (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, LandingPageSerializerSchema]]
    """


    return sync_detailed(
        domain_pk=domain_pk,
id=id,
client=client,
fields=fields,
period_from=period_from,
period_to=period_to,
filter_=filter_,

    ).parsed

async def asyncio_detailed(
    domain_pk: int,
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[LandingPageSerializerSchemaFields]] = UNSET,
    period_from: Union[Unset, None, str] = UNSET,
    period_to: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, int] = UNSET,

) -> Response[Union[Any, LandingPageSerializerSchema]]:
    """
    Args:
        domain_pk (int):
        id (int):
        fields (Union[Unset, None, str]):
        period_from (Union[Unset, None, str]):
        period_to (Union[Unset, None, str]):
        filter_ (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, LandingPageSerializerSchema]]
    """


    kwargs = _get_kwargs(
        domain_pk=domain_pk,
id=id,
client=client,
fields=fields,
period_from=period_from,
period_to=period_to,
filter_=filter_,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    domain_pk: int,
    id: int,
    *,
    client: Client,
    fields: Union[Unset, List[LandingPageSerializerSchemaFields]] = UNSET,
    period_from: Union[Unset, None, str] = UNSET,
    period_to: Union[Unset, None, str] = UNSET,
    filter_: Union[Unset, None, int] = UNSET,

) -> Optional[Union[Any, LandingPageSerializerSchema]]:
    """
    Args:
        domain_pk (int):
        id (int):
        fields (Union[Unset, None, str]):
        period_from (Union[Unset, None, str]):
        period_to (Union[Unset, None, str]):
        filter_ (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, LandingPageSerializerSchema]]
    """


    return (await asyncio_detailed(
        domain_pk=domain_pk,
id=id,
client=client,
fields=fields,
period_from=period_from,
period_to=period_to,
filter_=filter_,

    )).parsed

