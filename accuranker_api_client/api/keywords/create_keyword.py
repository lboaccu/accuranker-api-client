from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.keyword_in import KeywordIn
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: KeywordIn,

) -> Dict[str, Any]:
    url = "{}/keyword/".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Message]:
    if response.status_code == 202:
        response_202 = Message.from_dict(response.json())



        return response_202
    return None


def _build_response(*, response: httpx.Response) -> Response[Message]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeywordIn,

) -> Response[Message]:
    """Create a new keyword

     Creates a new keyword on a domain. The keyword can only created on domains authorized from the token
    provided.
        If no search settings are provided, the default search settings from the domain will be used.
        This endpoints starts a job to import your keywords. The response header 'Location' points to a
    specific endpoint for monitoring the status of your keyword job. Curl example:

        curl -X POST \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain_id\\": {your domain id}, \\"keywords\\":[\\"keyword 1\\", \\"keyword 2\\"]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (KeywordIn):

    Returns:
        Response[Message]
    """


    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: AuthenticatedClient,
    json_body: KeywordIn,

) -> Optional[Message]:
    """Create a new keyword

     Creates a new keyword on a domain. The keyword can only created on domains authorized from the token
    provided.
        If no search settings are provided, the default search settings from the domain will be used.
        This endpoints starts a job to import your keywords. The response header 'Location' points to a
    specific endpoint for monitoring the status of your keyword job. Curl example:

        curl -X POST \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain_id\\": {your domain id}, \\"keywords\\":[\\"keyword 1\\", \\"keyword 2\\"]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (KeywordIn):

    Returns:
        Response[Message]
    """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeywordIn,

) -> Response[Message]:
    """Create a new keyword

     Creates a new keyword on a domain. The keyword can only created on domains authorized from the token
    provided.
        If no search settings are provided, the default search settings from the domain will be used.
        This endpoints starts a job to import your keywords. The response header 'Location' points to a
    specific endpoint for monitoring the status of your keyword job. Curl example:

        curl -X POST \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain_id\\": {your domain id}, \\"keywords\\":[\\"keyword 1\\", \\"keyword 2\\"]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (KeywordIn):

    Returns:
        Response[Message]
    """


    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: KeywordIn,

) -> Optional[Message]:
    """Create a new keyword

     Creates a new keyword on a domain. The keyword can only created on domains authorized from the token
    provided.
        If no search settings are provided, the default search settings from the domain will be used.
        This endpoints starts a job to import your keywords. The response header 'Location' points to a
    specific endpoint for monitoring the status of your keyword job. Curl example:

        curl -X POST \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain_id\\": {your domain id}, \\"keywords\\":[\\"keyword 1\\", \\"keyword 2\\"]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (KeywordIn):

    Returns:
        Response[Message]
    """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed

