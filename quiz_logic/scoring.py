def calculate_score(user_answers):
    """Calculate the score based on user answers compared to correct answers."""
    score = 0
    for question, answer_data in user_answers.items():
        if answer_data['selected'] == answer_data['correct']:
            score += 1
    return score
