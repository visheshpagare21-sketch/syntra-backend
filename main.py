from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(
    api_key="AIzaSyCNqwTElUw7qAHR6cLhdSRJyRZm5HDH6RU"
)

@app.get("/")
def home():
    return {
        "message":"Syntra AI Running"
    }

@app.get("/chat")
def chat(q: str):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=q
        )

        return {
            "answer": response.text
        }

    except Exception as e:

        return {
            "answer": str(e)
        }