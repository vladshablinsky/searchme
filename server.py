import cherrypy
import os
from controllers import Root, Upload, SearchGenerator


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
    print config
    cherrypy.tree.mount(Root(), '/', config=config)
    cherrypy.tree.mount(Upload(), '/upload', config=config)
    cherrypy.tree.mount(SearchGenerator(), '/generate', config=config)
    return cherrypy.tree


def start():
    get_app()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    start()
