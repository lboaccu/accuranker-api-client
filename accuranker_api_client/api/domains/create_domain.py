from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.domain_schema_out import DomainSchemaOut
from ...models.domain_schema_validated import DomainSchemaValidated
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: DomainSchemaValidated,

) -> Dict[str, Any]:
    url = "{}/domain/".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[DomainSchemaOut]:
    if response.status_code == 201:
        response_201 = DomainSchemaOut.from_dict(response.json())



        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[DomainSchemaOut]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DomainSchemaValidated,

) -> Response[DomainSchemaOut]:
    """Create a new domain

     Creates a new domain for your group. A domain can only be created on groups or subaccounts
    authorized by the token provided. Curl example:

        curl -X POST \
            -H \"Authorization: Token {your api_token here}\" \
            -d \"{\\"domain\\":\\"Domain
    name\\",\\"default_searchsettings_names\\":[{\\"countrylocale\\":\\"en-GB\\",\\"search_engine_names\
    \":[{\\"search_engine\\":\\"Google\\",\\"search_type_names\\":[\\"Desktop\\"]}],\\"locations\\":[\\"
    BuckinghamPalace,London\\"]}],\\"group_id\\":{your group id here}}\" \
            https://app.accuranker.com/domain/



    Args:
        json_body (DomainSchemaValidated):

    Returns:
        Response[DomainSchemaOut]
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
    json_body: DomainSchemaValidated,

) -> Optional[DomainSchemaOut]:
    """Create a new domain

     Creates a new domain for your group. A domain can only be created on groups or subaccounts
    authorized by the token provided. Curl example:

        curl -X POST \
            -H \"Authorization: Token {your api_token here}\" \
            -d \"{\\"domain\\":\\"Domain
    name\\",\\"default_searchsettings_names\\":[{\\"countrylocale\\":\\"en-GB\\",\\"search_engine_names\
    \":[{\\"search_engine\\":\\"Google\\",\\"search_type_names\\":[\\"Desktop\\"]}],\\"locations\\":[\\"
    BuckinghamPalace,London\\"]}],\\"group_id\\":{your group id here}}\" \
            https://app.accuranker.com/domain/



    Args:
        json_body (DomainSchemaValidated):

    Returns:
        Response[DomainSchemaOut]
    """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DomainSchemaValidated,

) -> Response[DomainSchemaOut]:
    """Create a new domain

     Creates a new domain for your group. A domain can only be created on groups or subaccounts
    authorized by the token provided. Curl example:

        curl -X POST \
            -H \"Authorization: Token {your api_token here}\" \
            -d \"{\\"domain\\":\\"Domain
    name\\",\\"default_searchsettings_names\\":[{\\"countrylocale\\":\\"en-GB\\",\\"search_engine_names\
    \":[{\\"search_engine\\":\\"Google\\",\\"search_type_names\\":[\\"Desktop\\"]}],\\"locations\\":[\\"
    BuckinghamPalace,London\\"]}],\\"group_id\\":{your group id here}}\" \
            https://app.accuranker.com/domain/



    Args:
        json_body (DomainSchemaValidated):

    Returns:
        Response[DomainSchemaOut]
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
    json_body: DomainSchemaValidated,

) -> Optional[DomainSchemaOut]:
    """Create a new domain

     Creates a new domain for your group. A domain can only be created on groups or subaccounts
    authorized by the token provided. Curl example:

        curl -X POST \
            -H \"Authorization: Token {your api_token here}\" \
            -d \"{\\"domain\\":\\"Domain
    name\\",\\"default_searchsettings_names\\":[{\\"countrylocale\\":\\"en-GB\\",\\"search_engine_names\
    \":[{\\"search_engine\\":\\"Google\\",\\"search_type_names\\":[\\"Desktop\\"]}],\\"locations\\":[\\"
    BuckinghamPalace,London\\"]}],\\"group_id\\":{your group id here}}\" \
            https://app.accuranker.com/domain/



    Args:
        json_body (DomainSchemaValidated):

    Returns:
        Response[DomainSchemaOut]
    """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed

