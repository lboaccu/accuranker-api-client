from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.group_update import GroupUpdate
from ...models.group_update_out import GroupUpdateOut
from ...types import Response


def _get_kwargs(
    group_id: int,
    *,
    client: AuthenticatedClient,
    json_body: GroupUpdate,

) -> Dict[str, Any]:
    url = "{}/group/{group_id}".format(
        client.base_url,group_id=group_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GroupUpdateOut]:
    if response.status_code == 200:
        response_200 = GroupUpdateOut.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GroupUpdateOut]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    json_body: GroupUpdate,

) -> Response[GroupUpdateOut]:
    """Update a group

     Update a group for your organization. Only groups on organizations or subaccounts authorized from
    the token provided can be updated. \"
        \"All fields are optional. If you leave a field out, the value will not be updated. Curl
    example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"\"{\\"name\\":\\"Group name\\",\\"organization_id\\":{your organization id here}}\"\" \
        https://app.accuranker.com/group/{you group id here}


    Args:
        group_id (int): Id of the group you want to update
        json_body (GroupUpdate):

    Returns:
        Response[GroupUpdateOut]
    """


    kwargs = _get_kwargs(
        group_id=group_id,
client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    json_body: GroupUpdate,

) -> Optional[GroupUpdateOut]:
    """Update a group

     Update a group for your organization. Only groups on organizations or subaccounts authorized from
    the token provided can be updated. \"
        \"All fields are optional. If you leave a field out, the value will not be updated. Curl
    example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"\"{\\"name\\":\\"Group name\\",\\"organization_id\\":{your organization id here}}\"\" \
        https://app.accuranker.com/group/{you group id here}


    Args:
        group_id (int): Id of the group you want to update
        json_body (GroupUpdate):

    Returns:
        Response[GroupUpdateOut]
    """


    return sync_detailed(
        group_id=group_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    json_body: GroupUpdate,

) -> Response[GroupUpdateOut]:
    """Update a group

     Update a group for your organization. Only groups on organizations or subaccounts authorized from
    the token provided can be updated. \"
        \"All fields are optional. If you leave a field out, the value will not be updated. Curl
    example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"\"{\\"name\\":\\"Group name\\",\\"organization_id\\":{your organization id here}}\"\" \
        https://app.accuranker.com/group/{you group id here}


    Args:
        group_id (int): Id of the group you want to update
        json_body (GroupUpdate):

    Returns:
        Response[GroupUpdateOut]
    """


    kwargs = _get_kwargs(
        group_id=group_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    json_body: GroupUpdate,

) -> Optional[GroupUpdateOut]:
    """Update a group

     Update a group for your organization. Only groups on organizations or subaccounts authorized from
    the token provided can be updated. \"
        \"All fields are optional. If you leave a field out, the value will not be updated. Curl
    example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"\"{\\"name\\":\\"Group name\\",\\"organization_id\\":{your organization id here}}\"\" \
        https://app.accuranker.com/group/{you group id here}


    Args:
        group_id (int): Id of the group you want to update
        json_body (GroupUpdate):

    Returns:
        Response[GroupUpdateOut]
    """


    return (await asyncio_detailed(
        group_id=group_id,
client=client,
json_body=json_body,

    )).parsed

