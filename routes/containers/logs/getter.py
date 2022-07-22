from common_funcs.api_request import make_get_async_request_data


async def get_containers_logs(container_id: str) -> str:
    url = f'http://localhost:2300/containers/{container_id}/logs?stdout=True'
    try:
        data = await make_get_async_request_data(url)
    except UnicodeDecodeError:
        try:
            url = f'http://localhost:2300/containers/{container_id}/logs?stream=1'
            data = await make_get_async_request_data(url)
            return data
        except Exception as e:
            raise Exception(f'Ошибка при получении логов: {e}')
    return data
