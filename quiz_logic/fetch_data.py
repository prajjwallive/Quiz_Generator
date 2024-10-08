import requests

def fetch_data_from_wikipedia(category):
    """Fetch relevant data from Wikipedia based on the selected category."""
    search_terms = {
        'Animals': 'largest mammals',
        'Sports': 'Olympics',
        'Science': 'scientific discoveries',
        'History': 'ancient civilizations'
    }
    
    if category in search_terms:
        query = search_terms[category]
        url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json'
        response = requests.get(url)
        data = response.json().get('query', {}).get('search', [])
        
        print(f"Fetched Data for {category}: {data}")  # Debug statement to see fetched data
        return data
    else:
        raise ValueError("Unsupported category")
