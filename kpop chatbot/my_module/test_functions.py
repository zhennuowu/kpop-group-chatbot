"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import ask_of_year, greeting_chat

def test_ask_of_year():
    
    assert callable(ask_of_year)
    assert isinstance(ask_of_year(True, 'okay'), str)
    assert ask_of_year(False,'okay') == None
    assert isinstance(ask_of_year(True, 'yes'), str)
    assert ask_of_year(False, 'no') == None


def test_greeting_chat():    
    assert callable(greeting_chat)
    assert greeting_chat(False) == None
    assert greeting_chat(True) == "hi! I can help you to know more about K-pop."
    assert isinstance(greeting_chat(True), str)
    assert greeting_chat(0) == None
                 
    