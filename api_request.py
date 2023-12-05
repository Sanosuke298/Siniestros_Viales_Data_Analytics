import requests

# Define the API endpoint URL
base_url = "https://apitransporte.buenosaires.gob.ar"  # Updated base URL

# Define the endpoint path you want to access
endpoint_path = "/datos/movilidad/transito"

# Define your client ID and client secret
client_id = "17d8ae9888ce46e08078f88caafa9393"
client_secret = "6aFc3F721BE94031B2aBaaDFc548905d"

# Construct the full URL with the endpoint
url = f"{base_url}{endpoint_path}"

# Create headers with the client ID and client secret for authentication
headers = {
    "client_id": client_id,  # Corrected header name
    "client_secret": client_secret  # Corrected header name
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # You can now work with the response data, which is in JSON format
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")
