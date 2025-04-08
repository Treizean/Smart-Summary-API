import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize this:\n{text}"}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response['choices'][0]['message']['content']