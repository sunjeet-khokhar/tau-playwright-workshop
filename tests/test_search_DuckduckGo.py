# to run headed --> python3 -m pytest tests/test_search_DuckduckGo.py  --headed --browser chromium  --slowmo 1000 -s
#to run headless --> python3 -m pytest tests/test_search_DuckduckGo.py --browser webkit  --slowmo 1000 -s

import pytest

ANIMALS = [
    'pickle',
    'python',
    'grizzly bear',
    'black mamba',
    'mccaw',
    'wolf',
    'panther',
    'tiger',
    'peacock'
]

TECH = [
    'butter'
]

@pytest.mark.parametrize('search_tech_keywords',TECH)
def test_duckduckgo_search(home_page,results_page,common_methods,search_tech_keywords):
    # Given the DuckDuckGo homepage is displayed
    # when the user searches for a seach term
    #then the search result results are related to that term 
    #and the title of the page also reflects that term 
    
    ''' Original code that has been refactored to use POM and PyTest fixtures
    page.fill("[id='search_form_input_homepage']",'pickles')
    page.click("[id='search_button_homepage']")
    assert 'pickles' == page.input_value("#search_form_input")
    #wait for some result titles to load , being defensive
    page.locator("[data-testid=result-title-a] >> nth=4").wait_for()
    page_titles = page.locator("[data-testid=result-title-a]").all_inner_texts()
    print(len(page_titles))
    assert len(page_titles) >0 
    for t in page_titles: 
        print(t)
        # weak test !
        assert('pick' in t.lower())
    assert('pickle' in page.title().lower())'''
    
    
    home_page.load()
    home_page.enter_search_term(search_tech_keywords)
    home_page.press_search_button()
    assert search_tech_keywords == results_page.get_search_field_value()
    #wait for some result titles to load , being defensive
    results_page.wait_for_nth_result_to_load('4')
    page_titles=results_page.get_inner_text_of_all_results()
    print(len(page_titles))
    assert len(page_titles) >0 
    for t in page_titles: 
        print(t)
        # an example of a flaky test ..ask why?!
        #assert(search_term in t.lower())
    assert(search_tech_keywords in common_methods.get_title_of_page().lower())
        

    

