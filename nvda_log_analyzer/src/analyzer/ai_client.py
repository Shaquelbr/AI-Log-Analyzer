import os
import requests

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

NVIDIA_ENDPOINT = "https://integrate.api.nvidia.com/v1/chat/completions"

def summarize_logs(text):
    """Local fallback summarizer using simple heuristics"""
    lines = text.splitlines()
    short = [l for l in lines if len(l) < 200]
    return " | ".join(short[:10]) if short else text[:500]


def analyze_with_nim(text, model="meta/llama-3.1-8b-instruct"):
    if not NVIDIA_API_KEY:
        raise ValueError("NVIDIA_API_KEY environment variable is not set")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert system for identifying root causes in logs."},
            {"role": "user", "content": text}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NVIDIA_API_KEY}"
    }

    response = requests.post(NVIDIA_ENDPOINT, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]