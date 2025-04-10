# agents/chatbot_agent.py

import requests

# If using Ollama locally
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama2"  # or use 'mistral', 'gemma' etc.

def ask_farming_bot(question):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": question,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload)
        res.raise_for_status()
        return res.json()["response"].strip()
    except Exception as e:
        return f"⚠️ Error contacting LLM: {str(e)}"

# Example
if __name__ == "__main__":
    reply = ask_farming_bot("What crop should I grow in summer with low rainfall?")
    print("🤖", reply)
