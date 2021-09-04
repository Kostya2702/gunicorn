# WSGI APP for stepik
import re


def wsgi_app(environ):
    # start_responce('200', [('Content-type', 'text/plain')])
    pattern = r'.*?(\?\w)'
    body = re.findall(pattern, environ)
    print(body)


wsgi_app('/?a=1&a=2&b=3 ')

