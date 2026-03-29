# Access gemini model from vertex ai

from google.genai import Client
from google.oauth2.service_account import Credentials
api_key_path = "project-99973915-6ec0-4919-a49-4a99af956eb0.json"

credentials = Credentials.from_service_account_file(
    api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

PROJECT_ID =  "project-99973915-6ec0-4919-a49"
REGION = "us-central1"
MODEL_NAME = "gemini-2.5-flash"

client = Client(
    vertexai=True,
    project=PROJECT_ID,
    location=REGION,
    credentials=credentials
)

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="What is the color of Apple?"
)

print("Model Response:\n", response.text)