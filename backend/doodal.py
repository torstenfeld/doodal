__author__ = 'Torsten'

import json
import bottle

config = {
    'api': {
        'base1': '/api/1/'
    }
}

apiBase1 = config['api']['base1']


class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            bottle.response.headers['Access-Control-Allow-Origin'] = '*'
            bottle.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            bottle.response.content_type = 'application/json'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)
            print 'success'
        return _enable_cors


app = bottle.app()
app.install(EnableCors())


@app.route(apiBase1 + 'signup', method='POST')
@app.route(apiBase1 + 'signup', method='OPTIONS')
#@app.route('/api/1/signup', method='ANY')
def signup():
    if bottle.request.method == 'POST':
        print bottle.request.json
    return json.dumps({'success': '1'})

if __name__ == '__main__':
    app.run(server='paste', port=5000, debug=True, reloader=True)
