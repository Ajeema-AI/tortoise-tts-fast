import requests

# URL of the FastAPI app
url = "http://localhost:8000/generate/"

# Parameters
data = {
    "text": "Hello, this is a test.",
    "voice": "train_atkins",
    "preset": "fast"
}

# Send POST request
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Save the generated audio file
    with open('generated_speech.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file generated and saved as 'generated_speech.wav'.")
else:
    print("Failed to generate speech:", response.text)
