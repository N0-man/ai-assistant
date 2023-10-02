
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from pydantic import BaseModel

from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"
# choose documents
docnames = ["lm-pov.pdf"]
docfolders = ["docs"]
doc_index = 0

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(
        max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    chat_openai = ChatOpenAI(temperature=0, model_name=GPT_MODEL, max_tokens=num_outputs)
    llm_predictor = LLMPredictor(llm=chat_openai)

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index


def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

#########################
app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    source: str
    question: str


@app.get('/pulse')
async def pulse_check():
    print("I am checking pulse")
    return {'response: I am alive'}

@app.post('/ask')
async def ask_question(question_data: Item):
    question = question_data.question
    response = chatbot(question)
    return {'response': response}


if __name__ == "__main__":
    index = construct_index(docfolders[doc_index])
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
