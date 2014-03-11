
import robot.utils.asserts as asserts

from robotpageobjects.page import Page, robot_alias

class Page(Page):
    name = "Widget Page"
    uri = "/site/index.html"
    selectors = {"search-button": "go"}

    @robot_alias("search__name__for")
    def search(self, term):
        self.input_text("q", "search term")
        self.click_element("search-button")
        return SearchResultPage()


class SearchResultPage(Page):
    name = "Widget Search Result Page"
    selectors = {"results": "xpath=id('results')/li"}

    @robot_alias("__name__should_have_results")
    def should_have_results(self, expected):
        len_results = len(self.find_elements("results"))
        asserts.assert_equals(len_results, int(expected), "Unexpected number of results found on %s, got %s, "
                                                          "expected %s" %(self.name, len_results, expected))


