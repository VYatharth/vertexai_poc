#pip install google-genai
#pip install google-auth

from google.genai import Client

PROJECT_ID =  "proect-99973915-6ec0-4919-a49"
REGION = "us-central1"
MODEL_NAME = "gemini-2.5-flash"

client = Client(
    vertexai=True,
    project=PROJECT_ID,
    location=REGION,
)

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="What is the color of Apple"
)

print("Model Response:\n", response.text)
