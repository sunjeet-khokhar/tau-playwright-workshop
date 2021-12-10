"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""

from playwright.sync_api import Page

class ResultsPage:
    
    SEARCH_FIELD = "#search_form_input"
    RESULT_TITLES = "[data-testid=result-title-a]"
    
    
    def __init__(self,page : Page):
        self.page = page
        
    def get_search_field_value(self):
        return(self.page.input_value(self.SEARCH_FIELD))
    
    def wait_for_nth_result_to_load(self,num):
        self.page.locator(self.RESULT_TITLES + ">> nth=" +num).wait_for()
        
    def get_inner_text_of_all_results(self):
        return(self.page.locator(self.RESULT_TITLES).all_inner_texts())
    
    def get_title_of_page(self):
        return(self.page.title())