# ABDair AI

A modern AI-powered CLI assistant built with Python and Groq.

ABDair AI provides a developer-friendly terminal experience with streaming responses, persistent conversation history, retry handling, and automatic conversation summarization.

---

## Features

- Real-time streaming responses
- Persistent chat history
- Automatic conversation summarization
- Token usage tracking
- Retry handling for API failures
- Interactive CLI experience
- Environment-based configuration
- Custom commands system

---

## Preview

```bash
╔══════════════════════════════════════════╗
║        🤖 ABDair AI — CLI               ║
║              Powered by Groq            ║
╚══════════════════════════════════════════╝

👤 You: Explain Python decorators

🤖 Assistant:
Python decorators are functions that modify the behavior
of another function without changing its code...
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/abdair-coca/abdAIr.git
cd abdAIr
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -e .
```

---

## 4. Configure environment variables

Create a `.env` file in the project root:

```env
API_KEY=your_groq_api_key
MODEL=llama3-70b-8192
```

---

# Usage

Run the assistant from anywhere in your terminal:

```bash
abdair chat
```
or
```bash
abdair 
```

---

# Available Commands

| Command | Description |
|---|---|
| `/ayuda` | Show available commands |
| `/salir` | Exit the assistant |
| `/limpiar` | Clear conversation history |
| `/historial` | Show current chat history |
| `/tokens` | Display token usage |
| `/guardar` | Save chat history |
| `/resumir` | Summarize conversation |

---

# Project Structure

```text
abdair-ai/
│
├── assistant/
│   ├── __init__.py
│   ├── cli.py
│   ├── main.py
│   ├── chat.py
│   ├── commands.py
│   ├── history.py
│   ├── config.py
│   └── ui.py
│
├── .env
├── .gitignore
├── historial.json
├── pyproject.toml
└── README.md
```

---

# Technologies Used

- Python
- Groq API
- Typer
- python-dotenv

---

# Future Improvements

- Rich terminal UI
- Markdown rendering
- Syntax highlighting
- File system tools
- Tool calling
- Multi-model support
- Agent workflows
- Voice support
- Plugin system

---

# Contributing

Pull requests are welcome.

If you'd like to contribute, feel free to fork the repository and submit improvements.

---

# License

This project is licensed under the MIT License.

---

# Author

Built by Abdair.
