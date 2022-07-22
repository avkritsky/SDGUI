import json
from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from common_funcs.api_request import make_get_async_request, make_post_async_request, make_get_async_request_data

router = APIRouter(
    prefix="/containers",
    tags=["containers"],
)

templates = Jinja2Templates(directory='templates')


@router.get('/inspect/{container_id}')
async def restart_container(request: Request, container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/json'
    data: dict = await make_get_async_request(url)
    if data:
        # reworked_data = rework_data_for_html(data)
        # for key, item in data.items():
        #     if isinstance(item, list):
        #         data[key] = rework_list(item)
        #     elif isinstance(item, dict):
        #         data[key] = rework_dict(item)
        response = {'request': request, 'data': data}
        return templates.TemplateResponse('inspect.html', response)
    else:
        return RedirectResponse('/')


def rework_data_for_html(raw_data: dict):

    ...
    return raw_data


def rework_list(raw_list: list) -> list:
    res = []

    for val in raw_list:
        if isinstance(val, list):
            res.append(f'{rework_list(val)} ')
        elif isinstance(val, dict):
            res.append(f'{rework_dict(val)} ')
        else:
            res.append(f'{val} ')
    return res


def rework_dict(raw_list: dict) -> list:
    res = []

    for key, val in raw_list.items():
        if isinstance(val, list):
            res.append(f'{key}:')
            res.append(f'{rework_list(val)} ')
        elif isinstance(val, dict):
            res.append(f'{key}:')
            res.append(f'{rework_dict(val)} ')
        else:
            res.append(f'{key}:')
            res.append(f'{val} ')

    return res


@router.get('/restart/{container_id}')
async def restart_container(container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/restart'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/start/{container_id}')
async def restart_container(container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/start'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/stop/{container_id}')
async def restart_container(container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/stop'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/pause/{container_id}')
async def pause_container(container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/pause'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/unpause/{container_id}')
async def unpause_container(container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/unpause'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/logs/{container_id}')
async def unpause_container(request: Request, container_id: str, selected_range: int = 1):
    LOG_RANGE = 40
    url = f'http://localhost:2300/containers/{container_id}/logs?stdout=True'
    try:
        data = await make_get_async_request_data(url)

    except UnicodeDecodeError as e:
        try:
            url = f'http://localhost:2300/containers/{container_id}/logs?stream=1'
            data = await make_get_async_request_data(url)
            return data
        except Exception as e:
            print(f'ffff {e}')
            data = {'data': e}
            return data

    logs_lines = data.split('\n')[::-1] * 2

    ranged_logs_lines = [logs_lines[i: i + LOG_RANGE] for i in range(0, len(logs_lines), LOG_RANGE)]

    data = {'logs': ranged_logs_lines[selected_range],
            'name': container_id,
            'request': request,
            'col': len(ranged_logs_lines),
            }
    return templates.TemplateResponse('logs.html', data)
