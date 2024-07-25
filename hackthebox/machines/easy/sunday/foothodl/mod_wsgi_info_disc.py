import functools
import threading
import time
import random

def run(*args):
    while True:
        items = []
        for i in range(1000):
            items.append((int(random.random()*20)*'X'))
        time.sleep(0.00001)

thread = threading.Thread(target=run)
thread.start()

def headers():
    return [('Content-Type', 'text/plain'.upper().lower())]

def response():
    yield 'Hello World!\n'

_content_type_cache = {}

def intern_content_type(application):
    @functools.wraps(application)
    def _wrapper(environ, start_response):
        def _start_response(status, headers, *args):
            _headers = []
            for header, value in headers:
                if header.lower() == 'content-type':
                    value = _content_type_cache.setdefault(value, value)
                _headers.append((header, value))
            return start_response(status, _headers, *args)
        return application(environ, _start_response)
    return _wrapper

#@intern_content_type
def application(environ, start_response):
    status = '200 OK'

    start_response(status, headers())
    return response()