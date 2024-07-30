import requests
import json

# Define the URL
url = "https://dps-challenge.netlify.app/.netlify/functions/api/challenge"

# Define the payload
payload = {
    "github": "https://github.com/SK-tec/AccidentForecaster",
    "email": "samathagamidi@gmail.com",
    "url": "https://serene-thicket-27393-a24abd46fe60.herokuapp.com/",
    "notes": "I deployed using Heroku..."
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Print the response
if response.status_code==200:
    print("Status Code:", response.status_code)
    print("Congratulations! Achieved Mission 3")
else:
    print("Failed to submit:", response.json())
