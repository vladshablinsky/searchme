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
        SearchModel.add_query_to_file(SearchModel(), searchquery)
        return MainView.get_all_querries(MainView())


class Upload(object):
    @cherrypy.expose
    def index(self, myFile=None):
        filename = UploadModel.upload_file(UploadModel(), myFile)
        return MainView.get_file_added(MainView(), filename)
