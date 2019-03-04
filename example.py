import requests
improt logging
logging.basicConfig(level=logging.DEBUG)
urls = [
    'http://python-requests.org',
    'http://httpbin.org',
    'http://python-guide.org',
    'http://kennethreitz.com'
]

def do_something(response):
    print( response.url())

async_list = []
for u in urls:
    action_item = async.get(u)
    async_list.append(action_item)

async.map(async_list)
