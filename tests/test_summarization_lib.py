import unittest
from unittest.mock import patch, MagicMock
from summarization_lib import (
    initialize_cohere_model,
    split_text_into_chunks,
    create_documents_from_chunks,
    get_custom_prompt,
    create_summarization_chain,
    generate_summary,
    format_summary,
)
from langchain.docstore.document import Document


class TestSummarizationLib(unittest.TestCase):

    @patch("summarization_lib.Cohere")
    def test_initialize_cohere_model(self, mock_cohere):
        api_key = "test_api_key"
        model_name = "test_model"

        mock_model = MagicMock()
        mock_cohere.return_value = mock_model

        model = initialize_cohere_model(api_key, model_name)

        mock_cohere.assert_called_once_with(model=model_name)
        self.assertEqual(model, mock_model)

    def test_split_text_into_chunks(self):
        text = "This is a long text. " * 100
        chunk_size = 50
        chunk_overlap = 10

        chunks = split_text_into_chunks(text, chunk_size, chunk_overlap)

        self.assertTrue(all(len(chunk) <= chunk_size for chunk in chunks))
        self.assertGreater(len(chunks), 1)

    def test_create_documents_from_chunks(self):
        chunks = ["Chunk 1", "Chunk 2", "Chunk 3"]
        documents = create_documents_from_chunks(chunks)

        self.assertEqual(len(documents), len(chunks))
        self.assertTrue(all(isinstance(doc, Document) for doc in documents))

    def test_get_custom_prompt(self):
        prompt = get_custom_prompt()
        self.assertIn("Write a concise summary of the following text:", prompt.template)
        self.assertIn("CONCISE SUMMARY:", prompt.template)
        self.assertIn("text", prompt.input_variables)

    @patch("summarization_lib.load_summarize_chain")
    def test_create_summarization_chain(self, mock_load_summarize_chain):
        llm = MagicMock()
        custom_prompt = MagicMock()

        chain = MagicMock()
        mock_load_summarize_chain.return_value = chain

        result = create_summarization_chain(llm, custom_prompt)

        mock_load_summarize_chain.assert_called_once_with(
            llm,
            chain_type="map_reduce",
            map_prompt=custom_prompt,
            combine_prompt=custom_prompt,
        )
        self.assertEqual(result, chain)

    def test_generate_summary(self):
        chain = MagicMock()
        documents = [Document(page_content="Sample text")]

        chain.run.return_value = "Summary text"

        summary = generate_summary(chain, documents)

        chain.run.assert_called_once_with(documents)
        self.assertEqual(summary, "Summary text")

    def test_format_summary(self):
        output_summary = "This is a long summary text that should be wrapped. " * 5
        formatted = format_summary(output_summary, width=50)

        self.assertTrue(all(len(line) <= 50 for line in formatted.splitlines()))


if __name__ == "__main__":
    unittest.main()
