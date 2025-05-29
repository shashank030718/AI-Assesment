from agents.retriever_agent import retrieve
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your-key"  # or load from .env

client = OpenAI()

def generate_brief(query):
    context = retrieve(query)
    prompt = (
        f"Context:\n{context[0]}\n{context[1]}\n\n"
        f"Question: {query}\n"
        f"Answer:"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
