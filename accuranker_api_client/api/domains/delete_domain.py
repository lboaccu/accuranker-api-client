from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    domain_id: int,
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/domain/{domain_id}".format(
        client.base_url,domain_id=domain_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Message]:
    if response.status_code == 200:
        response_200 = Message.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Message]:
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

) -> Response[Message]:
    """Delete a domain

     Deletes a domain and all underlying keywords. Eventhough it is possible, for our support team, to
    restore deleted domains, you should use this end point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to delete

    Returns:
        Response[Message]
    """


    kwargs = _get_kwargs(
        domain_id=domain_id,
client=client,

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

) -> Optional[Message]:
    """Delete a domain

     Deletes a domain and all underlying keywords. Eventhough it is possible, for our support team, to
    restore deleted domains, you should use this end point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to delete

    Returns:
        Response[Message]
    """


    return sync_detailed(
        domain_id=domain_id,
client=client,

    ).parsed

async def asyncio_detailed(
    domain_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Message]:
    """Delete a domain

     Deletes a domain and all underlying keywords. Eventhough it is possible, for our support team, to
    restore deleted domains, you should use this end point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to delete

    Returns:
        Response[Message]
    """


    kwargs = _get_kwargs(
        domain_id=domain_id,
client=client,

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

) -> Optional[Message]:
    """Delete a domain

     Deletes a domain and all underlying keywords. Eventhough it is possible, for our support team, to
    restore deleted domains, you should use this end point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to delete

    Returns:
        Response[Message]
    """


    return (await asyncio_detailed(
        domain_id=domain_id,
client=client,

    )).parsed

