"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from playwright.sync_api import Page

class HomePage:
    HOME_URL = 'https://www.duckduckgo.com/'
    
    SEARCH_BOX = "[id='search_form_input_homepage']"
    SEARCH_BUTTON = "[id='search_button_homepage']"
    
    def __init__(self,page : Page):
        self.page = page
        
    
    def load(self):
        self.page.goto(self.HOME_URL)

    def enter_search_term(self,term):
        self.page.fill(self.SEARCH_BOX,term)
        
    def press_search_button(self):
        self.page.click(self.SEARCH_BUTTON)