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


def start():
    get_app()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    start()
