from typing import Tuple
from common_funcs.api_request import make_get_async_request_data


async def get_containers_logs(container_id: str) -> Tuple[int, str]:
    url = f'http://localhost:2300/containers/{container_id}/logs?stdout=True&tail=1000'
    try:
        status_code, data = await make_get_async_request_data(url)
    except Exception as e:
        print(e)
        return 503, str(e)
    return status_code, data
