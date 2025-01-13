import os
from langchain_community.llms import Cohere  # pylint: disable=E0611
from langchain.chains import load_summarize_chain  # pylint: disable=E0611
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import textwrap

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


# Initialize the Cohere LLM
def initialize_cohere_model(api_key: str, model_name: str = "command-xlarge"):
    os.environ["COHERE_API_KEY"] = api_key
    return Cohere(model=model_name)


# Split text into manageable chunks
def split_text_into_chunks(text: str, chunk_size: int = 1000, chunk_overlap: int = 200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return text_splitter.split_text(text)


# Convert text chunks into LangChain document format
def create_documents_from_chunks(chunks: list[str]):
    return [
        Document(page_content=chunk) for chunk in chunks[:10]
    ]  # Reduce the number of the chunks to reduce tokens


# Define a custom summarization prompt
def get_custom_prompt():
    prompt_template = """Write a concise summary of the following text:

    {text}

    CONCISE SUMMARY:"""
    return PromptTemplate(template=prompt_template, input_variables=["text"])


# Create the summarization chain
def create_summarization_chain(llm, custom_prompt):
    return load_summarize_chain(
        llm,
        chain_type="map_reduce",
        map_prompt=custom_prompt,
        combine_prompt=custom_prompt,
    )


# Generate the summary
def generate_summary(chain, documents):
    return chain.run(documents)


# Format the output
def format_summary(output_summary, width: int = 100):
    return textwrap.fill(
        output_summary, width=width, break_long_words=False, replace_whitespace=False
    )