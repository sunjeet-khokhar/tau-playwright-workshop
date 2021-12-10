"""
This module contains shared fixtures.
"""
import pytest 
from pages.search_sk import HomePage
from pages.result_sk import ResultsPage
from pages.common import CommonMethods

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def results_page(page):
    return ResultsPage(page)

@pytest.fixture
def common_methods(page):
    return CommonMethods(page)

