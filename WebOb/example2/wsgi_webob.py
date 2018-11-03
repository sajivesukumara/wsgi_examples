
from webob import Response
from webob.dec import wsgify

from paste import httpserver
from paste.deploy import loadapp

INI_PATH='/root/paste_example/WebOb/example2/wsgi_webob.ini'

@wsgify
def application(request):
    return Response("Hello, Welcome to WebOb")

def app_factory(global_config, **local_config):
    return application

@wsgify.middleware
def auth_filter(request, app):
    print("Request [%s] " % dir(request.headers))
    print("Authentication token [%s] " % request.headers.get('X-Auth-Token'))
    if request.headers.get('X-Auth-Token') != 'hpinvent':
          return exc.HTTPForbidden()
    print(dir(app))
    return app(request)

def filter_factory(global_config, **local_config):
    return auth_filter

wsgi_app = loadapp('config:' + INI_PATH, name="mymain")
httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)

