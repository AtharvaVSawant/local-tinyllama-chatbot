# 🦙 Local TinyLlama Chatbot

A lightweight, fully offline AI chatbot powered by **TinyLlama** running locally on your machine — no internet required, no API keys, complete privacy.

---

## 📸 Screenshots

> _Chat Interface_

![Chat Interface](Chatbot.png)

---

## 🚀 Features

- 💻 Runs **100% locally** — no cloud, no API keys
- 🦙 Powered by **TinyLlama** (1.1B parameter model)
- ⚡ Fast responses with low hardware requirements
- 🔒 Complete privacy — your data never leaves your machine
- 🖥️ Simple and clean chat interface

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | TinyLlama 1.1B |
| Backend | Python |
| Interface | (e.g. Streamlit / Gradio / CLI) |
| Runtime | Ollama / llama.cpp / LlamaCpp Python |

> _(Update the table above to match your actual stack)_

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) _(or your chosen runtime)_

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/AtharvaVSawant/local-tinyllama-chatbot.git
cd local-tinyllama-chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull the TinyLlama model (if using Ollama)
ollama pull tinyllama

# 4. Run the chatbot
python app.py
```

---

## 💬 Usage

1. Launch the app using the command above
2. Type your message in the chat input
3. Get instant responses from TinyLlama — all locally!

---

## 📁 Project Structure

```
local-tinyllama-chatbot/
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
├── screenshots/         # UI screenshots
│   ├── screenshot1.png
│   └── screenshot2.png
└── README.md
```

---

## ⚙️ Configuration

You can tweak model parameters in `app.py`:

```python
# Example config
model = "tinyllama"
temperature = 0.7
max_tokens = 512
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT](LICENSE)

---

## 👤 Author

**Atharva Sawant**  
GitHub: [@AtharvaVSawant](https://github.com/AtharvaVSawant)
