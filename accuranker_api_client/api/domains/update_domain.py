from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.domain_schema_out import DomainSchemaOut
from ...models.domain_schema_update_validated import DomainSchemaUpdateValidated
from ...types import Response


def _get_kwargs(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    json_body: DomainSchemaUpdateValidated,

) -> Dict[str, Any]:
    url = "{}/domain/{domain_id}".format(
        client.base_url,domain_id=domain_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[DomainSchemaOut]:
    if response.status_code == 200:
        response_200 = DomainSchemaOut.from_dict(response.json())



        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DomainSchemaOut]:
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
    json_body: DomainSchemaUpdateValidated,

) -> Response[DomainSchemaOut]:
    """Update a domain

     Update a domain in your group. All fields are optional. If you leave a field out, the value will not
    be updated.
        The exception is sub-fields to default_searchsettings_names: the entire
    default_searchsettings_names objects will overwrite whatever exists on the domain. Curl example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain\\":\\"Domain name\\", \\"display_name\\": \\"Domain display name\\"}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to update
        json_body (DomainSchemaUpdateValidated):

    Returns:
        Response[DomainSchemaOut]
    """


    kwargs = _get_kwargs(
        domain_id=domain_id,
client=client,
json_body=json_body,

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
    json_body: DomainSchemaUpdateValidated,

) -> Optional[DomainSchemaOut]:
    """Update a domain

     Update a domain in your group. All fields are optional. If you leave a field out, the value will not
    be updated.
        The exception is sub-fields to default_searchsettings_names: the entire
    default_searchsettings_names objects will overwrite whatever exists on the domain. Curl example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain\\":\\"Domain name\\", \\"display_name\\": \\"Domain display name\\"}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to update
        json_body (DomainSchemaUpdateValidated):

    Returns:
        Response[DomainSchemaOut]
    """


    return sync_detailed(
        domain_id=domain_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    domain_id: int,
    *,
    client: AuthenticatedClient,
    json_body: DomainSchemaUpdateValidated,

) -> Response[DomainSchemaOut]:
    """Update a domain

     Update a domain in your group. All fields are optional. If you leave a field out, the value will not
    be updated.
        The exception is sub-fields to default_searchsettings_names: the entire
    default_searchsettings_names objects will overwrite whatever exists on the domain. Curl example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain\\":\\"Domain name\\", \\"display_name\\": \\"Domain display name\\"}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to update
        json_body (DomainSchemaUpdateValidated):

    Returns:
        Response[DomainSchemaOut]
    """


    kwargs = _get_kwargs(
        domain_id=domain_id,
client=client,
json_body=json_body,

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
    json_body: DomainSchemaUpdateValidated,

) -> Optional[DomainSchemaOut]:
    """Update a domain

     Update a domain in your group. All fields are optional. If you leave a field out, the value will not
    be updated.
        The exception is sub-fields to default_searchsettings_names: the entire
    default_searchsettings_names objects will overwrite whatever exists on the domain. Curl example:

        curl -X PUT \
        -H \"Authorization: Token {your api_token here}\" \
        -d \"{\\"domain\\":\\"Domain name\\", \\"display_name\\": \\"Domain display name\\"}\" \
        https://app.accuranker.com/domain/{you domain id here}


    Args:
        domain_id (int): Id of the domain you want to update
        json_body (DomainSchemaUpdateValidated):

    Returns:
        Response[DomainSchemaOut]
    """


    return (await asyncio_detailed(
        domain_id=domain_id,
client=client,
json_body=json_body,

    )).parsed

