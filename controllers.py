import cherrypy
from views import MainView
from models import SearchModel, UploadModel


class Root(object):
    @cherrypy.expose
    def index(self):
        return MainView.get_index(MainView())


class SearchGenerator(object):
    @cherrypy.expose
    def index(self, searchquery):
        sm = SearchModel()
        mv = MainView()
        sm.search_in_database(searchquery)
        return mv.get_search_results(sm.matches)


class Upload(object):
    @cherrypy.expose
    def index(self, myFile=None):
        um = UploadModel()
        mv = MainView()
        filename = um.upload_file(myFile)
        return mv.get_file_added(filename)
