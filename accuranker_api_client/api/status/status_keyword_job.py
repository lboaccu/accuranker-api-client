from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/status/keyword_job/{job_id}".format(
        client.base_url,job_id=job_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Message]:
    if response.status_code == 200:
        response_200 = Message.from_dict(response.json())



        return response_200
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
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Message]:
    """Status of keyword job

     Return status of an keyword job, given a job ID. To start a job call POST or PUT /keyword.
        Any response code other than 200 means the job is not finished or failed.
        Response code 200 means the job is finished and the keywords should be available on your domain.
    Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/status/keyword_job/{your job id}


    Args:
        job_id (str):

    Returns:
        Response[Message]
    """


    kwargs = _get_kwargs(
        job_id=job_id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Message]:
    """Status of keyword job

     Return status of an keyword job, given a job ID. To start a job call POST or PUT /keyword.
        Any response code other than 200 means the job is not finished or failed.
        Response code 200 means the job is finished and the keywords should be available on your domain.
    Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/status/keyword_job/{your job id}


    Args:
        job_id (str):

    Returns:
        Response[Message]
    """


    return sync_detailed(
        job_id=job_id,
client=client,

    ).parsed

async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Message]:
    """Status of keyword job

     Return status of an keyword job, given a job ID. To start a job call POST or PUT /keyword.
        Any response code other than 200 means the job is not finished or failed.
        Response code 200 means the job is finished and the keywords should be available on your domain.
    Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/status/keyword_job/{your job id}


    Args:
        job_id (str):

    Returns:
        Response[Message]
    """


    kwargs = _get_kwargs(
        job_id=job_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Message]:
    """Status of keyword job

     Return status of an keyword job, given a job ID. To start a job call POST or PUT /keyword.
        Any response code other than 200 means the job is not finished or failed.
        Response code 200 means the job is finished and the keywords should be available on your domain.
    Curl example:

        curl -X GET \
        -H \"Authorization: Token {your api_token here}\" \
        https://app.accuranker.com/status/keyword_job/{your job id}


    Args:
        job_id (str):

    Returns:
        Response[Message]
    """


    return (await asyncio_detailed(
        job_id=job_id,
client=client,

    )).parsed

