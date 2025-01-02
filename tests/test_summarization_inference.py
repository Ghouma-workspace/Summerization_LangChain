import unittest
from unittest.mock import patch, mock_open
from summarization_inference import main


class TestSummarizationInference(unittest.TestCase):

    @patch("summarization_inference.initialize_cohere_model")
    @patch("summarization_inference.split_text_into_chunks")
    @patch("summarization_inference.create_documents_from_chunks")
    @patch("summarization_inference.get_custom_prompt")
    @patch("summarization_inference.create_summarization_chain")
    @patch("summarization_inference.generate_summary")
    @patch("summarization_inference.format_summary")
    @patch(
        "builtins.open", new_callable=mock_open, read_data="This is a test document."
    )
    def test_main(
        self,
        mock_open_file,
        mock_format_summary,
        mock_generate_summary,
        mock_create_chain,
        mock_get_prompt,
        mock_create_docs,
        mock_split_text,
        mock_initialize_model,
    ):
        # Mock outputs
        mock_llm = "MockLLM"
        mock_initialize_model.return_value = mock_llm
        mock_split_text.return_value = ["Chunk 1", "Chunk 2"]
        mock_create_docs.return_value = [
            {"page_content": "Chunk 1"},
            {"page_content": "Chunk 2"},
        ]
        mock_get_prompt.return_value = "MockPrompt"
        mock_chain = "MockChain"
        mock_create_chain.return_value = mock_chain
        mock_generate_summary.return_value = "Summary text."
        mock_format_summary.return_value = "Formatted summary."

        # Run main function
        input_file = "test_file.txt"
        api_key = "test_api_key"
        main(input_file, api_key)

        # Assertions
        mock_open_file.assert_called_once_with(input_file, "r", encoding="utf-8")
        mock_initialize_model.assert_called_once_with(api_key)
        mock_split_text.assert_called_once()
        mock_create_docs.assert_called_once()
        mock_get_prompt.assert_called_once()
        mock_create_chain.assert_called_once_with(mock_llm, "MockPrompt")
        mock_generate_summary.assert_called_once_with(
            mock_chain, mock_create_docs.return_value
        )
        mock_format_summary.assert_called_once_with("Summary text.")


if __name__ == "__main__":
    unittest.main()
