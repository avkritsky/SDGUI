from typing import Tuple
from common_funcs.api_request import make_get_async_request_data


async def get_containers_logs(container_id: str) -> Tuple[int, str]:
    url = f'http://localhost:2300/containers/{container_id}/logs?stdout=True'
    try:
        status_code, data = await make_get_async_request_data(url)
    except UnicodeDecodeError:
        try:
            url = f'http://localhost:2300/containers/{container_id}/logs?stream=1'
            status_code, data = await make_get_async_request_data(url)
            return status_code, data
        except Exception as e:
            return 503, str(e)
    return status_code, data
