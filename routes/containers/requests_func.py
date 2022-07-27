from typing import Callable

from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from common_funcs.api_request import make_post_async_request

templates = Jinja2Templates(directory='templates')

async def make_request(url: str,
                       request: Request,
                       request_func: Callable = make_post_async_request,
                       success_code: int = 204):
    status_code, data = await request_func(url, data={})
    if status_code == success_code:
        return RedirectResponse('/')
    response = {'request': request, **data}
    return templates.TemplateResponse('error_page.html', response)