from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_returns_cat_fact_mock():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact": "In 1987 cats overtook dogs as the number one pet in America.", "length": 60}
    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: In 1987 cats overtook dogs as the number one pet in America."