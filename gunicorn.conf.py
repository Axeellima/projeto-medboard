import os
import ipdb

def post_request(worker, req, environ, resp):
    if not req.is_keepalive():
        ipdb.set_trace()

bind = '0.0.0.0:8000'
workers = 4
accesslog = '-'
errorlog = '-'
loglevel = 'info'
post_request = post_request

# Add WhiteNoiseMiddleware
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
