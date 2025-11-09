import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel Python handler - simplified and optimized
def handler(request):
    # Vercel's @vercel/python runtime expects a handler that receives a request
    # and returns a response. The runtime handles WSGI conversion automatically.
    # We need to properly format the response.
    
    # Build WSGI environ from Vercel request
    environ = {
        'REQUEST_METHOD': request.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': request.path or '/',
        'QUERY_STRING': str(request.query_string or ''),
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': request.headers.get('content-length', ''),
        'SERVER_NAME': request.headers.get('host', 'localhost').split(':')[0],
        'SERVER_PORT': '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': getattr(request, 'body', None),
        'wsgi.errors': None,
        'wsgi.multithread': False,
        'wsgi.multiprocess': True,
        'wsgi.run_once': False,
    }
    
    # Add HTTP headers
    for key, value in request.headers.items():
        key_upper = key.upper().replace('-', '_')
        if key_upper not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{key_upper}'] = value
    
    # Response storage
    response_headers = []
    status_code = [200]
    
    def start_response(status, headers):
        status_code[0] = status
        response_headers[:] = headers
    
    # Call Flask app
    response = app(environ, start_response)
    
    # Build response body
    body_parts = []
    for part in response:
        if isinstance(part, bytes):
            body_parts.append(part)
        else:
            body_parts.append(part.encode('utf-8'))
    
    body = b''.join(body_parts).decode('utf-8') if body_parts else ''
    
    return {
        'statusCode': int(status_code[0].split()[0]),
        'headers': dict(response_headers),
        'body': body
    }
