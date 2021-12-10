

def test_duckduckgo_search(home_page,results_page,common_methods):
    # Given the DuckDuckGo homepage is diisplayed
    # when the user searches for pickles
    #then the search result results are related to pickles 
    #and the title of the page also reflects pickles 
    
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
    
    search_term = 'pickles'
    home_page.load()
    home_page.enter_search_term(search_term)
    home_page.press_search_button()
    assert search_term == results_page.get_search_field_value()
    #wait for some result titles to load , being defensive
    results_page.wait_for_nth_result_to_load('4')
    page_titles=results_page.get_inner_text_of_all_results()
    print(len(page_titles))
    assert len(page_titles) >0 
    for t in page_titles: 
        print(t)
        # weak test !
        assert('pick' in t.lower())
    assert('pickle1' in common_methods.get_title_of_page().lower())
        

    

