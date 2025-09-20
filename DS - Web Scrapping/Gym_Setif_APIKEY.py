import requests

def get_popular_gyms(api_key, location, radius=5000, type='gym'):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'type': type,
        'key': api_key
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        gyms = response.json().get('results', [])
        for gym in gyms:
            name = gym.get('name')
            address = gym.get('vicinity')
            rating = gym.get('rating')
            print(f"Name: {name}, Address: {address}, Rating: {rating}")
    else:
        print(f"Error: {response.status_code}")

# Replace 'YOUR_API_KEY' with your actual Google Places API key
api_key = 'YOUR_API_KEY'
location = '36.1911,5.4137'  # Latitude and longitude for Setif, Algeria
get_popular_gyms(api_key, location)
