import xapian
import hashlib
import os
import sys


class UploadModel:

    def get_file(self, myfile):
        return

    def upload_file(self, myfile, dbpath="db"):

        contents = myfile.file.read()
        contents.decode('utf-8', 'ignore')
        filename = hashlib.md5(contents).hexdigest() + ".txt"
        filepath = "lib/" + filename[:2] + "/" + filename[2:4] + "/"
        if not os.path.exists(os.path.dirname(filepath + filename)):
            os.makedirs(os.path.dirname(filepath))
        with open(filepath + filename, "w") as fileout:
            fileout.write(contents)

        # Indexing new file
        db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)
        indexer = xapian.TermGenerator()
        stemmer = xapian.Stem("english")
        indexer.set_stemmer(stemmer)
        doc = xapian.Document()
        doc.set_data(contents)
        doc.add_value(0, filepath + filename)
        indexer.set_document(doc)
        indexer.index_text(contents)

        # Use the identifier to prevent duplicating documents
        idterm = u"Q" + filename
        doc.add_boolean_term(idterm)
        db.replace_document(idterm, doc)

        return filename


class SearchModel:

    matches = None

    def add_query_to_file(self, query_string):
        with open("searchlog.txt", "ab") as myfile:
            myfile.write(query_string + '\n')

    def search_in_database(self, query_string, dbpath="db"):
        try:
            # Open the database for searching.
            db = xapian.Database(dbpath)

            # Start an enquire session.
            enquire = xapian.Enquire(db)

             # Parse the query string to produce a Xapian::Query object.
            qp = xapian.QueryParser()
            stemmer = xapian.Stem("english")
            qp.set_stemmer(stemmer)
            qp.set_database(db)
            qp.set_stemming_strategy(xapian.QueryParser.STEM_SOME)
            query = qp.parse_query(query_string)

            # TODO add logs

            # Find the top 10 results for the query.
            enquire.set_query(query)
            self.matches = enquire.get_mset(0, 10)
        except xapian.DatabaseModifiedError:
            db.reopen()
            raise
