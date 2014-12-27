import cherrypy
import os
from controllers import Root, Upload, SearchGenerator, Download


def get_app_config():
    return {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }


def get_app(config=None):
    config = config or get_app_config()
    root = Root()
    root.download = Download()
    cherrypy.tree.mount(root, '/', config="config/webapp.cfg")
    cherrypy.tree.mount(Upload(), '/upload', config="config/webapp.cfg")
    cherrypy.tree.mount(SearchGenerator(), '/generate', config="config/webapp.cfg")


if __name__ == '__main__':
    import tornado
    import tornado.httpserver
    import tornado.wsgi

    get_app()
    wsgiapp = cherrypy.tree
    cherrypy.config.update({'engine.autoreload.on': False})
    cherrypy.server.unsubscribe()
    cherrypy.engine.signals.subscribe()
    cherrypy.log.error_log.propagate = False
    cherrypy.engine.start()
    container = tornado.wsgi.WSGIContainer(wsgiapp)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8080)
    tornado.ioloop.PeriodicCallback(lambda: cherrypy.engine.publish('main'), 100).start()
    tornado.ioloop.IOLoop.instance().start()
