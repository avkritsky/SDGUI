from typing import Callable

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from common_funcs.api_request import (make_get_async_request,
                                      make_delete_async_request)
from routes.containers.logs.root_func import get_logs_for_container

from routes.containers.requests_func import make_request

router = APIRouter(
    prefix="/containers",
    tags=["containers"],
)

templates = Jinja2Templates(directory='templates')


@router.get('/inspect/{container_id}')
async def inspect_container(container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/json'
    status_code, data = await make_get_async_request(url)
    if status_code == 200:
        return data
    return RedirectResponse('/')


@router.get('/restart/{container_id}')
async def restart_container(request: Request, container_id: str):
    """Роут для перезапуска контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/restart'
    return await make_request(url, request)


@router.get('/start/{container_id}')
async def start_container(request: Request, container_id: str):
    """Роут для запуска контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/start'
    return await make_request(url, request)


@router.get('/stop/{container_id}')
async def stop_container(request: Request, container_id: str):
    """Роут для остановки контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/stop'
    return await make_request(url, request)


@router.get('/pause/{container_id}')
async def pause_container(request: Request, container_id: str):
    """Роут для приостановки работы контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/pause'
    return await make_request(url, request)


@router.get('/unpause/{container_id}')
async def unpause_container(request: Request, container_id: str):
    """Роут для продолжения работы контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/unpause'
    return await make_request(url, request)


@router.get('/delete/{container_id}')
async def delete_container(request: Request, container_id: str):
    """Роут для удаления контейнера"""
    url = f'http://localhost:2300/containers/{container_id}'
    return await make_request(url, request, make_delete_async_request)



@router.get('/logs/{container_id}')
async def logs_view(request: Request, container_id: str, selected_range: int = 1):
    """Роут для просмотра логов контейнера"""

    data = {
        **await get_logs_for_container(container_id, selected_range),
        'name': container_id,
        'request': request,
    }
    if 'message' in data:
        return templates.TemplateResponse('error_page.html', data)
    return templates.TemplateResponse('logs.html', data)

