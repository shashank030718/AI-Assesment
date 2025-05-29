from fastapi import FastAPI
from agents.language_agent import generate_brief
from agents.voice_agent import transcribe_voice, speak_text

app = FastAPI()

@app.get("/brief")
def morning_brief():
    query = "What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?"
    brief = generate_brief(query)
    speak_text(brief)
    return {"brief": brief}

@app.get("/voice-brief")
def voice_input_to_brief():
    query = transcribe_voice()
    print("You said:", query)
    response = generate_brief(query)
    speak_text(response)
    return {"query": query, "brief": response}
