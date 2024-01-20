import os

from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.llms.bedrock import Bedrock
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import JSONLoader
from pprint import pprint
from langchain_core.prompts import PromptTemplate

# Get region and profile from env
region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
profile = os.environ.get("AWS_PROFILE", "default")

# Set LLM and embeddings
model = Bedrock(
    model_id="anthropic.claude-v2",
    region_name=region,
    credentials_profile_name=profile,
    model_kwargs={"max_tokens_to_sample": 200},
)
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1")

# Define metadata extraction function so we can filter on sections and return deep links as sources
def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["section"] = record.get("section")
    metadata["source"] = record.get("deep_link")
    
    return metadata

# Import JSON FAQ File using JSONLoader

file_path='../../data/processed/faq_data/EN_SYR.json'

loader = JSONLoader(
    file_path=file_path,
    jq_schema=".[]",
    content_key="answer",
    metadata_func=metadata_func
)

data = loader.load()



embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v1", region_name="us-east-1"
)

vectorstore = Chroma.from_documents(documents=data, embedding=embeddings)

# Get retriever from vectorstore
retriever = vectorstore.as_retriever()

prompt_template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer from the provided context, just say that your training materials don't include this information, don't try to make up an answer.
Keep the answer as concise as possible.

{context}

Question: {question}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(prompt_template)

llm = Bedrock(model_id="amazon.titan-text-express-v1", model_kwargs={"maxTokenCount": 4000})

def format_docs(docs):
    formatted_docs = "\n\n".join(doc.page_content for doc in docs)
    urls = [doc.metadata.source for doc in docs]  # assuming each doc has a 'url' attribute
    return formatted_docs, urls


rag_chain_from_docs = (
    RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])[0]))
    | custom_rag_prompt
    | llm
    | StrOutputParser()
    | RunnablePassthrough.assign(urls=(lambda x: format_docs(x["context"])[1]))
)


rag_chain_with_source = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough(), "urls": RunnablePassthrough()}
).assign(answer=rag_chain_from_docs)


# Add typing for input
class Question(BaseModel):
    __root__: str

chain = rag_chain_with_source
