from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Claude mode to interact with the LLM by Sanket Parchande", description="This is a FastAPI application to interact with the Anthropic Claude API.", version="1.0.0")
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# REQUEST | RESPONSE

class ChatRequest(BaseModel):
    message: str
    max_tokens: int = 200

class ChatResponse(BaseModel):
    response: str
    model: str
    input_tokens: int
    output_tokens: int

@app.get('/')
def root():
    return{"status":"ok", "message": "Welcome to the Anthropic Claude API!_PRAKASH_SENAPATI"}

@app.post('/chatbot')
def chat_strem(req:ChatRequest):
    from fastapi.responses import StreamingResponse
    #WE CAN CHANGE MODEL WHICHEVER AVAILABLE
    def generate():
        with client.messages.stream(
            model="claude-sonnet-5-5",
            messages=[{"role": "user", "content": req.message}],
            max_tokens=req.max_tokens,
        ) as stream:
            for text in stream.text_stream:
                yield f"data: {text}\n\n"
        yield "data: [DONE]\n\n"    

    return StreamingResponse(generate(), media_type="text/event-stream")