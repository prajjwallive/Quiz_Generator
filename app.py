from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page for the quiz generator."""
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    """Fetch quiz questions based on the selected category and return them in JSON format."""
    category = request.json['category']
    questions = fetch_trivia_questions(category)
    return jsonify(questions)

def fetch_trivia_questions(category):
    """Fetch trivia questions from the Open Trivia Database."""
    category_map = {
        'Animals': 27,     # Animals category ID
        'Sports': 21,      # Sports category ID
        'Science': 17,     # Science category ID
        'History': 23      # History category ID
    }
    
    category_key = category_map.get(category, 9)  # Default to General Knowledge if category not found
    url = f"https://opentdb.com/api.php?amount=5&category={category_key}&type=multiple"
    
    response = requests.get(url)
    data = response.json()

    questions = []
    for item in data['results']:
        questions.append({
            'question': item['question'],
            'type': 'mcq',
            'options': item['incorrect_answers'] + [item['correct_answer']],
            'answer': item['correct_answer']  # Assume the correct answer is provided
        })
    
    return questions

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    """Receive user answers, calculate the score, and return it."""
    user_answers = request.json
    score = calculate_score(user_answers)
    return jsonify({'score': score})

def calculate_score(user_answers):
    """Calculate the score based on user answers compared to correct answers."""
    score = 0
    for question, answer_data in user_answers.items():
        if answer_data['selected'] == answer_data['correct']:
            score += 1
    return score

if __name__ == '__main__':
    app.run(debug=True)
