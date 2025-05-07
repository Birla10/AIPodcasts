import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from backend.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Initialize the TestClient with the FastAPI app
        self.client = TestClient(app)

    def test_home_endpoint(self):
        # Test the root endpoint
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "AI Podcast API is running!"})
        
    @patch('backend.app.AIConversation')  # Patch where it's used (in app.py)
    def test_generate_podcast_endpoint_success(self, MockAIConversation):
        # Create a mock instance
        mock_ai_convo = MockAIConversation.return_value
        mock_ai_convo.generate_conversation.return_value = None

        payload = {"topic": "Technology"}
        response = self.client.post("/generate-podcast/", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Podcast generated successfully"})
        mock_ai_convo.generate_conversation.assert_called_once_with("Technology")

    @patch('backend.app.AIConversation')  # Patch where it's used (in app.py)
    def test_generate_podcast_endpoint_failure(self, MockAIConversation):
        # Create a mock instance that raises an exception
        mock_ai_convo = MockAIConversation.return_value
        mock_ai_convo.generate_conversation.side_effect = Exception("API error")

        payload = {"topic": "Technology"}
        try:
            response = self.client.post("/generate-podcast/", json=payload)
        except Exception as e:
            # Handle the exception and check the response
            self.assertEqual(str(e), "API error")        
        
    def test_generate_podcast_endpoint_missing_topic(self):
        # Test the /generate-podcast/ endpoint with missing topic
        payload = {}
        response = self.client.post("/generate-podcast/", json=payload)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_generate_podcast_endpoint_invalid_topic(self):
        # Test the /generate-podcast/ endpoint with invalid topic type
        payload = {"topic": 12345}  # Invalid type, should be a string
        response = self.client.post("/generate-podcast/", json=payload)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

if __name__ == "__main__":
    unittest.main()