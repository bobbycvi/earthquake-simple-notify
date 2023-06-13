import os
import requests
import time
from colorama import Fore, Style
from datetime import datetime

def notify_terminal(message):
    # Display a formatted notification message in the terminal
    separator = f"\n{'=' * 50}\n\n"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"{Fore.GREEN}{Style.BRIGHT}{timestamp}\n{message}{Style.RESET_ALL}"
    os.system(f'echo -e "{separator}{formatted_message}{separator}"')

def check_earthquakes():
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
    response = requests.get(url)
    data = response.json()

    colors = [Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    color_index = 0

    for feature in data['features']:
        properties = feature['properties']
        place = properties['place']
        magnitude = properties['mag']
        coordinates = feature['geometry']['coordinates']

        if 'Romania' in place:
            color = colors[color_index % len(colors)]
            message = f"Earthquake in Romania!\nMagnitude: {magnitude}\nLocation: {place}\nCoordinates: {coordinates}"
            notify_terminal(f"{color}{Style.BRIGHT}{message}{Style.RESET_ALL}")
            color_index += 1

# Run the script every 10 minutes
while True:
    check_earthquakes()
    time.sleep(30)  # Sleep for 30s

