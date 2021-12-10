"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""

#from playwright.sync_api import Page

class CommonMethods:
    
    def __init__(self,page):
        self.page = page
    
    def get_title_of_page(self):
        return(self.page.title())