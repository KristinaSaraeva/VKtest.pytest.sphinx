import sys
import os
current_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.dirname(current_folder) 
path = os.path.join(parent_folder, 'vk')
sys.path.append(path)
import pytest

from calculations import extremely_low, extremely_high, abnormal,calculate_decision,final_decision

def test_extremely_low():
    assert extremely_low(10, 55, 0, 1.5) == True 
    assert extremely_low(15, 70, 2, 3.0) == None 

def test_extremely_high():
    assert extremely_high(25, 130, 5, 7) == True 
    assert extremely_high(18, 100, 3, 5) == None 

def test_abnormal():
    assert abnormal(10, 30, 2, 9) == True
    assert abnormal(18, 80, 3, 5) == None 

def test_calculate_decision_abnormal():
    assert calculate_decision(10, 30, 2, 9, 3) == 0
    assert calculate_decision(20, 50, 3, 5, 3) == 0
    assert calculate_decision(18, 80, 3, 10, 1) == 0
    assert calculate_decision(25, 100, 1, 5, 4) == 0

def test_calculate_decision_normal():
    assert calculate_decision(15, 65, 3, 2.5, 3) == 50
 

def test_calculate_decision_extremely_high():
    assert calculate_decision(25, 80, 5, 7, 2) == 50
    assert calculate_decision(25, 100, 5, 5, 4) == 100

def test_calculate_decision_extremely_low():
    assert calculate_decision(11, 50, 2, 3, 3) == 50 
    assert calculate_decision(15, 55, 1, 3, 1) == 100 

def test_final_decision(capsys):
    final_decision(60)
    captured = capsys.readouterr()
    assert "Percent of human: 60%" in captured.out  
    final_decision(40)
    captured = capsys.readouterr()
    assert "Percent of replicant: 60%" in captured.out  