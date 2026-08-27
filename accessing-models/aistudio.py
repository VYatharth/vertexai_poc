# pip install google-genai

from google import genai


def generate():
    client = genai.Client(
        api_key="<YOUR-API-KEY>",
    )

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents='What is the color of Apple?',
    )
    print(response.text)

if __name__ == "__main__":
    generate()
