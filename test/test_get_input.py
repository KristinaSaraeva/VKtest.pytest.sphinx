import sys
import os
current_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.dirname(current_folder) 
path = os.path.join(parent_folder, 'vk')
sys.path.append(path)
import pytest

from get_input import validate_input, capture_additional_variables, run_questionnaire

def test_capture_additional_variables_correct(monkeypatch):
    user_input = iter(["18", "65", "2", "4.0"])
    monkeypatch.setattr('builtins.input', lambda _: next(user_input)) 
    assert capture_additional_variables() == (18, 65, 2, 4.0)
    
def test_validate_input2(monkeypatch):
    user_input =  iter(["", "6", "2", "f"])
    a = monkeypatch.setattr('builtins.input', lambda _: next(user_input)) 
    variants = ['Option 1', 'Option 2', 'Option 3']
    assert validate_input(a, variants) == 2

def test_validate_input4(monkeypatch):
    user_input = iter(["", "6", "-2", "4"])
    a = monkeypatch.setattr('builtins.input', lambda _: next(user_input)) 
    variants = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    assert validate_input(a, variants) == 4

def test_run_questionnaire(monkeypatch,capsys):
    question = {"Question 0: How are you?": [
        {
            "answer": "I OK",
            "score": 2
        },
        {
            "answer": "I am fine, thank you",
            "score": 4
        },
        {
            "answer": "None of your business",
            "score": 1
        }
    ]
    }
    monkeypatch.setattr('builtins.input', lambda _: "2")
    run_questionnaire(question)
    expected = "None of your business"
    captured = capsys.readouterr()
    assert expected in captured.out