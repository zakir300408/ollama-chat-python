#!/usr/bin/env python3
"""
Simple chat client for interacting with a local Ollama LLM server.
"""

import os
import sys
import requests

# Default configuration (can be overridden via environment)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:12b")
API_ENDPOINT = f"{OLLAMA_URL}/v1/chat/completions"
TIMEOUT = 60  # seconds

def query(prompt: str) -> str:
    """
    Send a user prompt to the Ollama server and return the model's reply.

    Args:
        prompt: The text input from the user.

    Returns:
        The text of the model's response.

    Exits with error code 1 if the HTTP request fails.
    """
    session = requests.Session()
    session.trust_env = False  # ignore proxy settings

    try:
        resp = session.post(
            API_ENDPOINT,
            json={
                "model": OLLAMA_MODEL,
                "messages": [{"role": "user", "content": prompt}],
            },
            headers={"Content-Type": "application/json"},
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    return data["choices"][0]["message"]["content"]

def main():
    """
    Main REPL loop. Type 'exit' or 'quit' to end.
    """
    print(f"Connected to Ollama at {API_ENDPOINT}")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if prompt.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if not prompt:
            continue

        reply = query(prompt)
        print(f"{OLLAMA_MODEL} → {reply}\n")

if __name__ == "__main__":
    main()
