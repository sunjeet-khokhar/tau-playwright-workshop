
def test_duckduckgo_search(home_page):
    # Given the DuckDuckGo homepage is diisplayed
    # when the user searches for pickles
    #then the search result results are related to pickles 
    #and the title of the page also reflects pickles 
    
    home_page.load()
    '''page.fill("[id='search_form_input_homepage']",'pickles')
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
    

