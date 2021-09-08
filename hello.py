# WSGI APP for stepik


def wsgi_app(environ, start_responce):
    start_responce('200 OK', [('Content-type', 'text/plain')])
    pattern = r'(?:\w\=\d)+'
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body


# print(wsgi_app('/?a=1&a=2&b=3'))

