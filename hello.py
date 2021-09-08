# WSGI APP for stepik
import re


def wsgi_app(environ, start_responce):
    start_responce('200 OK', [('Content-type', 'text/plain')])
    pattern = r'(?:\w\=\d)+'
    body = [bytes(f'{el}\n', 'ascii') for el in re.findall(pattern, environ)]
    return body


# print(wsgi_app('/?a=1&a=2&b=3'))

