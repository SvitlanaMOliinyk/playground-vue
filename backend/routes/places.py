from flask import Blueprint, request
import requests
import os
from dotenv import load_dotenv

places_bp = Blueprint('places', __name__)
load_dotenv()
api_key = os.environ.get("API_KEY")


@places_bp.route('/selected', methods=['GET'])
def get_selected_places():
    position_latitude = float(request.args.get('lat'))
    position_longitude = float(request.args.get('lon'))
    query = request.args.get('query')

    url = f"https://api.myptv.com/geocoding/v1/places/by-text?searchText={query}&language=en&center={position_latitude},{position_longitude}&radius=5000"
    headers = {
        'apiKey': api_key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    # print(f"API Response: {response.text}")
    if 'places' in data and len(data['places']) > 0:
        places = data['places']
        coordinates = []
        for location in places:
            longitude = location['referencePosition']['longitude']
            latitude = location['referencePosition']['latitude']
            coordinates.append({'name': location['formattedAddress'], 'lat': latitude, 'lon': longitude})
            print("Coordinates", coordinates)
        return {'coordinates': coordinates}  # Return a valid response with the coordinates
    else:
        return {'coordinates': []}  # Return an empty array if no places are found
