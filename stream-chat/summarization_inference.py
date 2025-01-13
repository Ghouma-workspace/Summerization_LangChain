from summarization_lib import (
    initialize_cohere_model,
    split_text_into_chunks,
    create_documents_from_chunks,
    get_custom_prompt,
    create_summarization_chain,
    generate_summary,
    format_summary,
)


def summarize_text(document_text: str, api_key: str) -> str:
    # Initialize the Cohere model
    llm = initialize_cohere_model(api_key)

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

    # Format the summary
    return format_summary(summary)