from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from common_funcs.api_request import make_get_async_request, make_post_async_request

# импорт дополнительных router-ов
from routes.images import root_images
from routes.containers import root_containers

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# включение дополнительных router-ов
app.include_router(root_images.router)
app.include_router(root_containers.router)


@app.get('/')
async def main_root(request: Request):
    url = 'http://localhost:2300/containers/json?all=True'
    status_code, data = await make_get_async_request(url)
    if status_code == 200:
        response = {'request': request, 'data': data}
        # 'Id', 'Names', 'Image', 'ImageID', 'Command', 'Created', 'Ports', 'Labels', 'State', 'Status', 'HostConfig', 'NetworkSettings', 'Mounts'
        return templates.TemplateResponse('root.html', response)
    else:
        return templates.TemplateResponse('error_page.html', data)

