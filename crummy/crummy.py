import logging

from aiohttp import web
from aiohttp_jinja2 import render_template
from aiohttp_jinja2 import setup as setup_jinja2

from jinja2 import FileSystemLoader


routes = web.RouteTableDef()


COOKIE_USERNAME_KEY = 'crummy'


def get_username(request):
    return request.cookies.get(COOKIE_USERNAME_KEY)


def set_username(response, username):
    response.set_cookie(
        COOKIE_USERNAME_KEY,
        username,
    )

def del_username(response):
    response.del_cookie(COOKIE_USERNAME_KEY)


async def root_view(request, error=None):
    return render_template('index.html', request, {
        'user': get_username(request),
        'error': error,
    })

@routes.get('/')
async def root_get(request):
    return await root_view(request)


@routes.post('/')
async def root_post(request):
    data = await request.post()
    username = data.get('username')
    password = data.get('password')

    if not username:
        return await root_view(request)

    if username == 'admin':
        error = 'The password for admin is protected.'
        if password == 'protected':
            error = 'Not literally, silly.'
        return await root_view(request, error)

    response = web.HTTPFound('/flag')
    set_username(response, username)
    return response


async def flag_view(request):
    return render_template('flag.html', request, {
        'user': get_username(request),
    })


@routes.get('/logout')
async def logout_get(request):
    response = web.HTTPFound('/')
    del_username(response)
    return response


@routes.get('/flag')
async def flag_get(request):
    return await flag_view(request)


def main():
    logging.basicConfig(level=logging.INFO)

    app = web.Application()
    setup_jinja2(app, loader=FileSystemLoader('templates'))
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    exit(main())
