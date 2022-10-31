from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.delete_keyword_input import DeleteKeywordInput
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: DeleteKeywordInput,

) -> Dict[str, Any]:
    url = "{}/keyword/".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    *,
    client: AuthenticatedClient,
    json_body: DeleteKeywordInput,

) -> Response[Message]:
    """Delete a keyword

     Deletes a keyword. Eventhough it is possible to restore deleted keywords, you should use this end
    point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"keyword_ids\\":[{your keyword ids}]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (DeleteKeywordInput):

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
    json_body: DeleteKeywordInput,

) -> Optional[Message]:
    """Delete a keyword

     Deletes a keyword. Eventhough it is possible to restore deleted keywords, you should use this end
    point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"keyword_ids\\":[{your keyword ids}]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (DeleteKeywordInput):

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
    json_body: DeleteKeywordInput,

) -> Response[Message]:
    """Delete a keyword

     Deletes a keyword. Eventhough it is possible to restore deleted keywords, you should use this end
    point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"keyword_ids\\":[{your keyword ids}]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (DeleteKeywordInput):

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
    json_body: DeleteKeywordInput,

) -> Optional[Message]:
    """Delete a keyword

     Deletes a keyword. Eventhough it is possible to restore deleted keywords, you should use this end
    point with caution. Curl example:

        curl -X DELETE \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"keyword_ids\\":[{your keyword ids}]}\" \
        https://app.accuranker.com/keyword/


    Args:
        json_body (DeleteKeywordInput):

    Returns:
        Response[Message]
    """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed

