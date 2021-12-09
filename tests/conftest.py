"""
This module contains shared fixtures.
"""
import pytest 
from pages.search_sk import HomePage

@pytest.fixture
def home_page(page):
    return HomePage(page)

