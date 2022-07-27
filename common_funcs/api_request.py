from aiohttp import ClientSession


async def make_get_async_request(url: str):
    async with ClientSession() as sess:
        async with sess.get(url) as res:
            data = await res.json(content_type=None)
            return res.status, data


async def make_get_async_request_data(url: str):
    async with ClientSession() as sess:
        async with sess.get(url) as res:
            data = await res.content.read()
            print('test')
            try:
                data = data.decode(errors='ignore')
            except UnicodeDecodeError:
                data = data.decode(encoding='cp1251', errors='ignore')
            return res.status, data


async def make_post_async_request(url: str, data: dict):
    async with ClientSession() as sess:
        async with sess.post(url, data=data) as res:
            data = await res.json(content_type=None)
            return res.status, data


async def make_delete_async_request(url: str, data: dict):
    async with ClientSession() as sess:
        async with sess.delete(url, data=data) as res:
            data = await res.json(content_type=None)
            return res.status, data
        