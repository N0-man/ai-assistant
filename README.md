# Contextual AI Assistant

## Contextual Knowledge Assistant

The application would extract embeddings in chunks from all the PDF's in ./docs folder and then use the context to anser questions.
TODO: Test other file formats for context e.g. ppt, doc, html, epub etc

1. create a .env file with `OPENAI_API_KEY=<your key>`
2. Add some pdf's for context

### Run

```
pip install -r requirements.txt
python kai.py clean --all
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
