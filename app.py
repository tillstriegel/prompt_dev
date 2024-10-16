from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_json(user_prompt):
    prompt = open("prompts/json.md", "r").read()

    response = client.chat.completions.create(
        model="llama-3.2-1b-preview",
        messages=[
          {
            "role": "system",
            "content": prompt
          },
          {
            "role": "user",
            "content": "User: " + user_prompt.lower()
          }
        ],
        stream=False,
        max_tokens=100,
        temperature=0,
    )

    # Extract and print only the response text content
    content = response.choices[0].message.content
    print(content)

if __name__ == "__main__":
  import time
  start = time.time()
  get_json("Nenne die 5 wichtigsten Fakten über Napoleon Bonaparte.")
  get_json("Vergleiche Mac OS und Windows.")
  get_json("Erstelle eine Liste mit 5 beliebten Restaurants in Berlin.")
  end = time.time()
  print(f"Time taken: {end - start} seconds")
