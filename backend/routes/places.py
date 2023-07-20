from flask import Blueprint, request
import requests
import os
from dotenv import load_dotenv
import logging

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

    logging.info(f"Making API request to URL: {url}")

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'places' in data and len(data['places']) > 0:
        places = data['places']
        coordinates = []
        for location in places:
            longitude = location['referencePosition']['longitude']
            latitude = location['referencePosition']['latitude']
            coordinates.append(
                {'name': location['formattedAddress'], 'lat': latitude, 'lon': longitude})
            logging.debug(f"Coordinates: {coordinates}")

            logging.info(
                f"Found {len(coordinates)} places near coordinates: lat={position_latitude}, lon={position_longitude}")
        return {'coordinates': coordinates}
    else:
        logging.info("No places found near the given coordinates.")
        return {'coordinates': []}
