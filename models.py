import hashlib
import os


class UploadModel:

    def get_file(self, myfile):
        return

    def upload_file(self, myfile):
        contents = myfile.file.read()
        filename = hashlib.md5(contents).hexdigest() + ".txt"
        filepath = "lib/" + filename[:2] + "/" + filename[2:4] + "/"
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filepath))
        with open(filepath + filename, "w") as fileout:
            fileout.write(contents)
        return filename


class SearchModel:

    def add_query_to_file(self, querytext):
        with open("searchlog.txt", "ab") as myfile:
            myfile.write(querytext + '\n')
