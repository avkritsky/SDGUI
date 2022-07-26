from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from common_funcs.api_request import (make_get_async_request,
                                      make_post_async_request,
                                      make_delete_async_request)
from routes.containers.logs.root_func import get_logs_for_container

router = APIRouter(
    prefix="/containers",
    tags=["containers"],
)

templates = Jinja2Templates(directory='templates')


@router.get('/inspect/{container_id}')
async def inspect_container(request: Request, container_id: str):
    url = f'http://localhost:2300/containers/{container_id}/json'
    data: dict = await make_get_async_request(url)
    if data:
        # response = {'request': request, 'data': data}
        # return templates.TemplateResponse('inspect.html', response)
        return data
    else:
        return RedirectResponse('/')


@router.get('/restart/{container_id}')
async def restart_container(container_id: str):
    """Роут для перезапуска контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/restart'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/start/{container_id}')
async def start_container(container_id: str):
    """Роут для запуска контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/start'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/stop/{container_id}')
async def stop_container(container_id: str):
    """Роут для остановки контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/stop'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/pause/{container_id}')
async def pause_container(container_id: str):
    """Роут для приостановки работы контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/pause'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/unpause/{container_id}')
async def unpause_container(container_id: str):
    """Роут для продолжения работы контейнера"""
    url = f'http://localhost:2300/containers/{container_id}/unpause'
    await make_post_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/delete/{container_id}')
async def delete_container(container_id: str):
    """Роут для удаления контейнера"""
    url = f'http://localhost:2300/containers/{container_id}'
    await make_delete_async_request(url, data={})
    return RedirectResponse('/')


@router.get('/logs/{container_id}')
async def logs_view(request: Request, container_id: str, selected_range: int = 1):
    """Роут для просмотра логов контейнера"""

    data = {
        **await get_logs_for_container(container_id, selected_range),
        'name': container_id,
        'request': request,
    }
    if 'error' in data:
        return templates.TemplateResponse('error_page.html', data)

    return templates.TemplateResponse('logs.html', data)
