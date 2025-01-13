import sys
from summarization_lib import (
    initialize_cohere_model,
    split_text_into_chunks,
    create_documents_from_chunks,
    get_custom_prompt,
    create_summarization_chain,
    generate_summary,
    format_summary,
)


def main(input_file: str, api_key: str):
    # Initialize the Cohere model
    llm = initialize_cohere_model(api_key)

    # Load the document to summarize
    with open(input_file, "r", encoding="utf-8") as f:
        document_text = f.read()

    # Split the document into chunks
    text_chunks = split_text_into_chunks(document_text)

    # Convert text chunks into LangChain document format
    documents = create_documents_from_chunks(text_chunks)

    # Create a custom summarization prompt
    custom_prompt = get_custom_prompt()

    # Create the summarization chain
    chain = create_summarization_chain(llm, custom_prompt)

    # Generate the summary
    summary = generate_summary(chain, documents)

    # Format and print the summary
    formatted_summary = format_summary(summary)
    print("\nFinal Summary:\n")
    print(formatted_summary)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python summarization_inference.py <input_file> <api_key>")
        sys.exit(1)

    arg_file = sys.argv[1]
    arg_key = sys.argv[2]
    main(arg_file, arg_key)
