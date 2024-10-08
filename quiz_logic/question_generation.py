import openai
from config import OPENAI_API_KEY

# Set up the OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_quiz(category):
    """Generate quiz questions and options using the ChatGPT API."""
    prompt = f"Generate 5 quiz questions about {category} with multiple-choice answers, formatted as: Question? | Option 1 | Option 2 | Option 3."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Debug: Print the full API response
        print("Full API Response:", response)  # Log the entire response to debug
        
        # Extract the content from the API response
        questions_data = response.choices[0].message['content']
        
        print(f"ChatGPT Response: {questions_data}")  # Debug statement to see the formatted response
        
        questions = parse_questions(questions_data)
        return questions

    except Exception as e:
        print(f"Error during OpenAI API call: {e}")  # Log any errors that occur
        return []

def parse_questions(questions_data):
    """Parse the questions and options from the ChatGPT response."""
    questions = []
    lines = questions_data.strip().split('\n')
    
    for line in lines:
        # Expect each line to have a specific format, e.g., "Question? | Option 1 | Option 2 | Option 3"
        parts = line.split('|')  # Assuming questions and options are separated by a '|'
        
        # Validate that we have at least a question and one option
        if len(parts) >= 2:
            question = parts[0].strip()
            options = [option.strip() for option in parts[1:]]
            questions.append({
                'question': question,
                'type': 'mcq',
                'options': options,
                'answer': options[0]  # Assume the first option is the correct one
            })
        else:
            print(f"Invalid question format: {line}")  # Debugging for improperly formatted lines

    return questions
