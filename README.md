# ollama-chat-python
A simple, zero-dependency Python REPL client that connects to your locally-hosted Ollama HTTP server, just pull a model, run ollama serve, and start chatting.

# Ollama Chat Client

A simple, zero-dependency Python REPL for chatting with your locally-hosted Ollama LLM server.

## Prerequisites

- Python 3.7 or higher  
- Git  
- Ollama CLI

## 1. Install Ollama

### macOS

1. Go to https://ollama.com/download and download the macOS package.  
2. Unzip the archive and move **Ollama.app** into your **Applications** folder.  
3. Open Terminal and run:
   
```bash
   ollama --help
````

### Windows

1. Download **OllamaSetup.exe** from [https://ollama.com/download](https://ollama.com/download).
2. Run the installer and follow the prompts.
3. Open Command Prompt and run:

 ```bash
 ollama --help
 ```

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama --help
```

## 2. Download a Model

Pull the model you want to chat with. For example:

```bash
ollama pull gemma3:12b
```

Replace `gemma3:12b` with any model name from the Ollama library.

## 3. Start the Ollama Server

Run the HTTP server so the client can connect:

```bash
ollama serve
```

By default it listens on `http://127.0.0.1:11434`.

## 4. Clone This Repository

```bash
git clone https://github.com/zakir300408/ollama-chat-python.git
cd ollama-chat-client
```

## 5. Run and Chat

Start the REPL client:

```bash
python chat_client.py
```

* Type your message at the `You:` prompt.
* Enter `exit` or `quit` to end the session.

Example session:

```
Connected to Ollama at http://127.0.0.1:11434/v1/chat/completions
Type 'exit' or 'quit' to stop.

You: Hello, Ollama!
gemma3:12b → Hi there! How can I help you today?
```

## License

This project is released under the MIT License.

