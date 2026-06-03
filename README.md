# Local TinyLlama Chatbot

A simple AI chatbot built using Streamlit, LangChain, Hugging Face Transformers, and TinyLlama.

This project was created as a beginner-friendly introduction to local Large Language Models (LLMs), LangChain integration, and web application development using Streamlit.

---

## Overview

The chatbot loads the TinyLlama-1.1B-Chat model locally and allows users to ask questions through a Streamlit interface.

The goal of this project was to learn:

* Local LLM deployment
* LangChain fundamentals
* Hugging Face model integration
* Streamlit application development
* Basic prompt-response workflows

---

## Features

* Runs locally on your machine
* No external API key required
* Streamlit-based user interface
* LangChain integration
* Hugging Face model loading
* Simple question-answer interaction

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Hugging Face Transformers
* TinyLlama 1.1B Chat Model

---

## Project Structure

```text
local-tinyllama-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

### 1. Clone the Repository

```bash
https://github.com/AtharvaVSawant/local-tinyllama-chatbot/blob/main/README.md
```

### 2. Navigate to the Project Directory

```bash
cd local-tinyllama-chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal (typically `http://localhost:8501`) to interact with the chatbot.

---

## Model Used

**TinyLlama/TinyLlama-1.1B-Chat-v1.0**

TinyLlama is a lightweight open-source language model designed to run efficiently on consumer hardware while providing conversational capabilities.

---

## Limitations

This project uses a relatively small 1.1B parameter language model.

Because of this:

* Responses may occasionally contain factual inaccuracies
* Hallucinations can occur
* Complex reasoning tasks may produce incorrect results
* Performance is significantly lower than larger modern LLMs

Example:

> The model incorrectly stated that Pune is a capital city of Maharashtra, demonstrating a common hallucination issue found in smaller language models.

This project is intended primarily for learning and experimentation.

---

## What I Learned

Through this project, I learned:

* How language models generate responses
* How to run Hugging Face models locally
* How LangChain integrates with LLMs
* How to build interactive applications using Streamlit
* The strengths and limitations of small open-source models
* Common challenges such as hallucinations and factual errors

---

## Future Improvements

Planned enhancements include:

* Conversation memory
* Chat history support
* Retrieval-Augmented Generation (RAG)
* PDF Question Answering
* Better open-source models
* Model selection options
* Cloud deployment support
* Improved response accuracy

---

## Screenshots

Add screenshots of the application in the `screenshots/` folder and reference them here.

Example:

```markdown
![Chatbot Screenshot](screenshots/chatbot.png)
```

---

## License

This project is licensed under the MIT License.

---

## Author

**Atharva Sawant**

This project was built as part of my learning journey in Generative AI, LangChain, Hugging Face, and Streamlit application development.
