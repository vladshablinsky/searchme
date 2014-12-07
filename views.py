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
        return filename + " added"

    def get_all_querries(self):
        myfile = open("searchlog.txt", "r")
        content = ""
        for line in myfile:
            content += line + "<br>"
        return content
