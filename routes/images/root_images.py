from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from common_funcs.api_request import make_get_async_request, make_delete_async_request

router = APIRouter(
    prefix="/images",
    tags=["images"],
)

templates = Jinja2Templates(directory='templates')


@router.get('/')
async def images_root(request: Request = None):
    url = 'http://localhost:2300/images/json?all=True'
    status_code, data = await make_get_async_request(url)
    if status_code == 200:
        for item in data:
            item['Created'] = datetime.fromtimestamp(item.get('Created', 0))
        response = {'request': request, 'data': data}
        return templates.TemplateResponse('images.html', response)
    response = {'request': request, **data}
    return templates.TemplateResponse('error_page.html', response)


@router.get('/delete/{image_id}')
async def restart_container(request: Request, image_id: str):
    url = f'http://localhost:2300/images/{image_id}'
    status_code, data = await make_delete_async_request(url, data={})
    if status_code == 200:
        return RedirectResponse('/images')
    response = {'request': request, **data}
    return templates.TemplateResponse('error_page.html', response)
