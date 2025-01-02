# Import necessary modules
import os
# pylint: disable=no-name-in-module
# No-name-in_module even tho it works fine
from langchain.llms import Cohere
from langchain.chains import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import textwrap


os.environ["COHERE_API_KEY"] = "Uiz0n3PnZXiz6WQIw0pzJUZITei5eTxZd5C6BP7A"


def __main__():
    # Initialize the Cohere model
    llm = Cohere(model="command-xlarge")

    # Split the text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    # Load the document to summarize
    with open("./inference_files/how_to_win_friends.txt", encoding='utf-8') as f:
        how_to_win_friends = f.read()

    # Split the document into chunks
    texts = text_splitter.split_text(how_to_win_friends)

    # Convert text chunks into LangChain document format
    # docs = [Document(page_content=t) for t in texts[:4]]  # Process only the first 4 chunks for demo
    docs = [Document(page_content=t) for t in texts]

    # Define a custom summarization prompt
    prompt_template = """Write a concise summary of the following text:

    {text}

    CONCISE SUMMARY:"""

    custom_prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

    # Create and run the Map-Reduce summarization chain
    chain = load_summarize_chain(
        llm,
        chain_type="map_reduce",
        map_prompt=custom_prompt,
        combine_prompt=custom_prompt,
    )

    output_summary = chain.run(docs)

    # Format the output
    wrapped_text = textwrap.fill(
        output_summary, width=100, break_long_words=False, replace_whitespace=False
    )
    # wrapped_text = textwrap.fill(output_summary, width=100)

    print("\nFinal Summary:\n")
    print(wrapped_text)
