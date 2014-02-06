from EntrezPageLibrary import EntrezPageLibrary
from BooksPageLibrary import BooksPageLibrary


class PubmedPageLibrary(EntrezPageLibrary):
    name = "pubmed"
    homepage = "http://www.ncbi.nlm.nih.gov/pubmed"

    def find_related_data_to(self, dbname):
        self.se.wait_until_element_is_visible("rdDatabase")
        self.se.select_from_list_by_value("rdDatabase", dbname)
        self.se.wait_until_page_contains("NCBI Bookshelf books that cite the current articles")
        self.se.click_button("rdFind")

        # For demo purpose, hardcode the type of page returned
        return BooksPageLibrary()
    
    def __init__(self, *args, **kwargs):
        return super(PubmedPageLibrary, self).__init__(*args, **kwargs)