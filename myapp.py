import cherrypy
import os
from cherrypy.lib import static

class Root(object):
	@cherrypy.expose
	def index(self):
		return file('index.html')

class SearchGenerator(object):
	@cherrypy.expose
	def index(self, searchquery):
		return searchquery

class Upload(object):
	@cherrypy.expose
	def index(self, myFile = None):
		return myFile.filename

conf = {
	'/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
	'/generate': {
        },
	'/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
}

if __name__ == "__main__":
	cherrypy.tree.mount(Root(), '/')
	cherrypy.tree.mount(SearchGenerator(), '/generate')
	cherrypy.tree.mount(Upload(), '/upload', conf)
	cherrypy.engine.start()
	cherrypy.engine.block()