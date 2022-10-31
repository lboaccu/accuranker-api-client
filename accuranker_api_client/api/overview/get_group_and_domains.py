from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.organization_client_domain import OrganizationClientDomain
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    include_subaccounts: Union[Unset, None, bool] = False,

) -> Dict[str, Any]:
    url = "{}/overview/group_domains".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["include_subaccounts"] = include_subaccounts



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[OrganizationClientDomain]:
    if response.status_code == 200:
        response_200 = OrganizationClientDomain.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[OrganizationClientDomain]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include_subaccounts: Union[Unset, None, bool] = False,

) -> Response[OrganizationClientDomain]:
    """List all your groups and their domains.

     Returns list of all your groups and their domains. The list is based on the token provided. Curl
    example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/group_domains


    Args:
        include_subaccounts (Union[Unset, None, bool]): If true, returns the organizations, group
            and domains for your subaccounts as well.

    Returns:
        Response[OrganizationClientDomain]
    """


    kwargs = _get_kwargs(
        client=client,
include_subaccounts=include_subaccounts,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: AuthenticatedClient,
    include_subaccounts: Union[Unset, None, bool] = False,

) -> Optional[OrganizationClientDomain]:
    """List all your groups and their domains.

     Returns list of all your groups and their domains. The list is based on the token provided. Curl
    example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/group_domains


    Args:
        include_subaccounts (Union[Unset, None, bool]): If true, returns the organizations, group
            and domains for your subaccounts as well.

    Returns:
        Response[OrganizationClientDomain]
    """


    return sync_detailed(
        client=client,
include_subaccounts=include_subaccounts,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include_subaccounts: Union[Unset, None, bool] = False,

) -> Response[OrganizationClientDomain]:
    """List all your groups and their domains.

     Returns list of all your groups and their domains. The list is based on the token provided. Curl
    example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/group_domains


    Args:
        include_subaccounts (Union[Unset, None, bool]): If true, returns the organizations, group
            and domains for your subaccounts as well.

    Returns:
        Response[OrganizationClientDomain]
    """


    kwargs = _get_kwargs(
        client=client,
include_subaccounts=include_subaccounts,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include_subaccounts: Union[Unset, None, bool] = False,

) -> Optional[OrganizationClientDomain]:
    """List all your groups and their domains.

     Returns list of all your groups and their domains. The list is based on the token provided. Curl
    example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/overview/group_domains


    Args:
        include_subaccounts (Union[Unset, None, bool]): If true, returns the organizations, group
            and domains for your subaccounts as well.

    Returns:
        Response[OrganizationClientDomain]
    """


    return (await asyncio_detailed(
        client=client,
include_subaccounts=include_subaccounts,

    )).parsed

