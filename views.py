import xapian


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
        return filename + " was successfully added"

    def get_search_results(self, matches):
        results = ""
        results += str(matches.size()) + " results found" + "<br>"
        for m in matches:
            results += "%i: %i%% docid=%i + %s\n" % (m.rank + 1, m.percent, m.docid, m.document.get_data()) + "<br><br><br>"
        return results

    def get_all_querries(self):
        myfile = open("searchlog.txt", "r")
        content = ""
        for line in myfile:
            content += line + "<br>"
        return content
