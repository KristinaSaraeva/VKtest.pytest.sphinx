from calculations import calculate_decision,final_decision


def capture_additional_variables():
    """
    Captures additional physiological variables from user input.

    Returns:
    - tuple: A tuple containing the captured respiration, heart rate, blushing level, and pupillary dilation.
    """
    try:
        respiration = int(input("Respiration (BPM): "))
        heart_rate = int(input("Heart rate (BPM): "))
        blushing_level = int(input("Blushing level: "))
        pupillary_dilation = float(input("Pupillary dilation (mm): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return capture_additional_variables()
    
    return respiration, heart_rate, blushing_level, pupillary_dilation

def human_replicant_percentage(score):
    """
    Calculates the percentage of human replicant based on captured physiological variables and a score.

    Args:
    - score (int): The score for decision making.

    Returns:
    - int: The percentage value of human replicant.
    """
    respiration, heart_rate, blushing_level, pupillary_dilation = capture_additional_variables()
    percent_of_human = calculate_decision(respiration, heart_rate, blushing_level, pupillary_dilation, score)
    return percent_of_human

def validate_input(answer, variants):
    """
    Validates the user input for questionnaire answers.

    Args:
    - answer (str): The user's input.
    - variants (list): The list of answer variants for the question.

    Returns:
    - int: The validated answer as an integer.
    """
    valid_choices = [str(i) for i in range(1, len(variants) + 1)]
    while answer not in valid_choices:
        print("Invalid choice. Please try again.")
        answer = input("Enter your choice: ")
    return int(answer)

def run_questionnaire(questions):
    """
    Runs a questionnaire and calculates the final decision based on the user's responses.

    Args:
    - questions (dict): A dictionary containing the questions and answer variants.

    Returns:
    - None
    """
    responses = []
    total_score = 0

    for question, variants in questions.items():
        print(question)
        for i, variant in enumerate(variants):
            print(f"{i+1}. {variant['answer']}")
        answer = input("Enter your choice: ")
        validated_answer = validate_input(answer, variants)
        responses.append(validated_answer)
        total_score += human_replicant_percentage(variants[validated_answer - 1]['score'])

    final_decision(total_score/len(questions))
    print("\nThank you for completing the questionnaire!\n")


