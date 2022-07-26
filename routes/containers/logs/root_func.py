from routes.containers.logs.getter import get_containers_logs
from routes.containers.logs.formater import format_logs_data_for_output


async def get_logs_for_container(container_id: str, selected_range: int = 1) -> dict:
    # получение логов
    status_code, logs = await get_containers_logs(container_id)
    if status_code != 200:
        return {'message': logs}

    # формирование логов для выдачи
    data = format_logs_data_for_output(logs, selected_range)

    return data