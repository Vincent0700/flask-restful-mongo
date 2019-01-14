from app.common.config import cfg
from app import app

if __name__ == '__main__':
    host = cfg.get('server.host')
    port = cfg.getint('server.port')
    debug = cfg.getboolean('server.debug')
    app.run(host=host, port=port, debug=debug)
