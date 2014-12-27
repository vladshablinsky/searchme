import cherrypy
from views import MainView
from models import SearchModel, UploadModel
from cherrypy.lib.static import serve_file
import xapian


class Root(object):
    @cherrypy.expose
    def index(self):
        return MainView.get_index(MainView())


class SearchGenerator(object):
    @cherrypy.expose
    def index(self, searchquery):
        sm = SearchModel()
        mv = MainView()
        try:
            sm.search_in_database(searchquery)
        except xapian.DatabaseModifiedError:
            return mv.try_again
        return mv.get_search_results(sm.matches)


class Upload(object):
    @cherrypy.expose
    def index(self, myFile=None):
        um = UploadModel()
        mv = MainView()
        try:
            filename = um.upload_file(myFile)
            return mv.get_file_added(filename)
        except AttributeError:
            return mv.no_file_selected()


class Download(object):
    @cherrypy.expose
    def index(self, filepath):
        return serve_file(filepath, "application/x-download", "attachment")
