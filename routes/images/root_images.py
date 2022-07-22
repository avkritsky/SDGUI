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
    data = await make_get_async_request('http://localhost:2300/images/json?all=True')
    if data:
        for item in data:
            item['Created'] = datetime.fromtimestamp(item.get('Created', 0))
            # item['Id'] = item.get('Id', '')[7:]
        response = {'request': request, 'data': data}
        return templates.TemplateResponse('images.html', response)
    else:
        return {'error': True, 'response_code': data}


@router.get('/delete/{image_id}')
async def restart_container(image_id: str):
    url = f'http://localhost:2300/images/{image_id}'
    await make_delete_async_request(url, data={})
    return RedirectResponse('/images')
