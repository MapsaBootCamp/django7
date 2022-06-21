import aiohttp
from aiohttp import ClientSession
import asyncio
import json
import logging
import sys

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_divar_top(client, query_parameter):
    try:
        content = await get_json(client, 'https://api.divar.ir/v8/web-search/tehran' + query_parameter)
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logging.error(
            "aiohttp exception for %s [%s]: %s",
            query_parameter,
            getattr(e, "status", None),
            getattr(e, "message", None),
        )
        return
    except Exception as e:
        logging.error(
            "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
        )
        return
    else:
        data = json.loads(content.decode('utf-8'))
        for elm in data['widget_list'][1:6]:
            title = elm['data']['title']
            description = elm['data']['description']
            image_url = elm['data']['image']
            district = elm['data']['district']
            logging.info('Title: ' + title + ' : ' + 'Des: ' + description +
                         " img_url: " + '(' + image_url + ')' + " District: " + district + "\n")
        logging.info('DONE:' + query_parameter + '\n'+'\n')
        await asyncio.sleep(10)


async def main(loop):
    while True:
        async with ClientSession(loop=loop) as session:
            await asyncio.gather(get_divar_top(session, '/car?q=206'),
                                 get_divar_top(session, '/car?q=405'),
                                 get_divar_top(session, '/car?q=landcruiser'))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()