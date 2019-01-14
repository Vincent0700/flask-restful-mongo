def nocache(app):
    @app.after_request
    def add_header(resp):
        resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        resp.headers['Pragma'] = 'no-cache'
        resp.headers['Expires'] = '0'
        resp.headers['Cache-Control'] = 'public, max-age=0'
        return resp
