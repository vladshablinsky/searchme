import glob
import os.path
import xapian
import cherrypy


class MainView:
    def get_index(self):
        return file("index.html")

    def get_searchlog(self):
        return

    def get_uploaded(self):
        return

    def get_searchresults(self):
        return

    def get_file_added(self, filename):
        return filename + " was successfully added<br>" + "<a href = '/'>Go on start page</a>"

    def no_file_selected(self):
        html = ""
        html += "<h1>No file selected.</h1>"
        html += "<a href = '/'>Go on start page</a>"
        return html

    def get_search_results(self, matches):
        html = ""
        html += str(matches.size()) + " results found" + "<br>"
        for m in matches:
            html += "%i: %i%% docid=%i + %s\n" % (m.rank + 1, m.percent, m.docid, m.document.get_data()) + "<br>"
            absPath = os.path.abspath(m.document.get_value(0))
            html += '<a href="/download/?filepath=' + absPath + '">' + "Get file" + "</a><br/>"
        return html

    def get_all_querries(self):
        myfile = open("searchlog.txt", "r")
        content = ""
        for line in myfile:
            content += line + "<br>"
        return content
