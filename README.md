# Contextual AI Assistant

The goal is to build cohesive or contextual smart agents leveraging LLM.

_Prerequisite_

1. install dependencices

```
pip install -r requirements.txt
```

2. create a .env file with `OPENAI_API_KEY=<your key>`

## KAI (Knowledge AI Assistant)

KAI is mostly an LLM over set of documents (pdf, doc, html, epub etc). It leverages Embedding-based search to answer question from the context (documents).

> TODO: Test other file formats for context e.g. ppt, doc, html, epub etc

Add some pdf's for context in `./docs` folder\
[reference](https://cookbook.openai.com/examples/question_answering_using_embeddings): OpenAI cookbook

### Run

```
python kai.py clean --all
```

<br/>
<hr/>

## BAAI (Business Analysis AI Assistant)

BAAI can help breaking down business features into Epics > Stoires > Acceptance cirterias.

> _TODO_: extend the solution to groom stories with more validations and edge scenerios

`baai_context.br.py` have top 5 features on building Singapore Rental car system extarcted from GPT. The questions that were asked to GPT were (1) what are the probelms with Singapore rental car system (2) Given above context what are the top 5 features to implement \
[reference](https://learn.deeplearning.ai/chatgpt-prompt-eng): deeplearning.ai’s ChatGPT Prompt Engineering for Developers course

### Run

```
python baai.py clean --all
```

<br/>
<hr/>

## Simple REST API for Q&amp;A ChatBot based on PDF files (basic version)

This is just an alternate approach to use FastAPI to expose the application as REST endpoint

### Run

```
python main.py clean --all
```

### test API

Pulse Check

```
curl -X GET http://localhost:8001/pulse
```

Ask Question

```
curl -X POST -H "Content-Type: application/json" -d '{"source": "unknown", "question": "What is boo?"}' http://localhost:8001/ask
```
