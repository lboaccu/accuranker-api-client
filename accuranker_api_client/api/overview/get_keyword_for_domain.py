from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.keyword_out import KeywordOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    keyword_contains: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/overview/keywords_for_domain/{domain_id}".format(
        client.base_url,domain_id=domain_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["keyword_contains"] = keyword_contains



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[KeywordOut]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = KeywordOut.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[KeywordOut]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    keyword_contains: Union[Unset, None, str] = UNSET,

) -> Response[List[KeywordOut]]:
    """List all your keywords on the domain.

     Returns a list of all your keywords on the provided domain. Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/keywords_for_domain/{your domain id
    here}\?keyword_contains=test


    Args:
        domain_id (int): Id of the domain to get keywords for.
        keyword_contains (Union[Unset, None, str]): Only returns keyword that contains the value of
            keyword_contains

    Returns:
        Response[List[KeywordOut]]
    """


    kwargs = _get_kwargs(
        domain_id=domain_id,
client=client,
keyword_contains=keyword_contains,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    keyword_contains: Union[Unset, None, str] = UNSET,

) -> Optional[List[KeywordOut]]:
    """List all your keywords on the domain.

     Returns a list of all your keywords on the provided domain. Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/keywords_for_domain/{your domain id
    here}\?keyword_contains=test


    Args:
        domain_id (int): Id of the domain to get keywords for.
        keyword_contains (Union[Unset, None, str]): Only returns keyword that contains the value of
            keyword_contains

    Returns:
        Response[List[KeywordOut]]
    """


    return sync_detailed(
        domain_id=domain_id,
client=client,
keyword_contains=keyword_contains,

    ).parsed

async def asyncio_detailed(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    keyword_contains: Union[Unset, None, str] = UNSET,

) -> Response[List[KeywordOut]]:
    """List all your keywords on the domain.

     Returns a list of all your keywords on the provided domain. Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/keywords_for_domain/{your domain id
    here}\?keyword_contains=test


    Args:
        domain_id (int): Id of the domain to get keywords for.
        keyword_contains (Union[Unset, None, str]): Only returns keyword that contains the value of
            keyword_contains

    Returns:
        Response[List[KeywordOut]]
    """


    kwargs = _get_kwargs(
        domain_id=domain_id,
client=client,
keyword_contains=keyword_contains,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    keyword_contains: Union[Unset, None, str] = UNSET,

) -> Optional[List[KeywordOut]]:
    """List all your keywords on the domain.

     Returns a list of all your keywords on the provided domain. Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/keywords_for_domain/{your domain id
    here}\?keyword_contains=test


    Args:
        domain_id (int): Id of the domain to get keywords for.
        keyword_contains (Union[Unset, None, str]): Only returns keyword that contains the value of
            keyword_contains

    Returns:
        Response[List[KeywordOut]]
    """


    return (await asyncio_detailed(
        domain_id=domain_id,
client=client,
keyword_contains=keyword_contains,

    )).parsed

