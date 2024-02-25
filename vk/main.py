#!/usr/bin/env python3
from get_input import run_questionnaire
import json

if __name__ == "__main__":
    with open("VKTest.json", "r") as file:
        questions = json.load(file)
    run_questionnaire(questions)