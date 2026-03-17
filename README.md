# AI PDF RAG Chatbot

This is a simple project where I built a chatbot that can **read and answer questions from a PDF** using a local AI model.

Instead of just asking general questions, you can give it a document and it will answer based on that — kind of like ChatGPT, but for your own files.

---

## What this project does

* Takes a PDF file
* Breaks it into smaller chunks
* Finds the most relevant parts for your question
* Uses a local AI model to generate an answer

All of this runs **locally on your machine** (no paid APIs).

---

## Tech used

* Python
* LangChain
* Ollama
* Phi-3 (local LLM)
* ChromaDB

---

## How to run it

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/ai-pdf-rag-chatbot.git
cd ai-pdf-rag-chatbot
```

Create environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the model:

```bash
ollama run phi3
```

Then run the app:

```bash
python rag.py

## Example

```
Ask: What is this document about?
Ask: Summarize the main idea
Ask: Explain section 2
```

## Why I built this

I wanted to understand how real AI apps work beyond just calling an API.

This project helped me learn:

* how LLMs can use external data
* how embeddings and vector databases work
* how to build something practical with LangChain

## Improvements I plan to add

* A simple web UI (like ChatGPT)
* Support for multiple PDFs
* Better response accuracy

## Note
This runs fully locally using Ollama, so performance depends on your system.

Radheshyam Yadav
