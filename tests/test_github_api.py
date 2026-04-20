import unittest
from src.github_api import fetch_user_gists,run_fetch_user_gists
from src.github_api import save_last_run_timestamp
from unittest.mock import patch, Mock
import logging

class TestGitHubGistMonitor(unittest.TestCase):

    def setUp(self):
        # Configure the logger for test cases using the same setup_logger function
        self.logger = logging.getLogger("github_gists")
        self.logger.setLevel(logging.INFO)
    
    def tearDown(self):
        # Reset the logger's state to avoid interference with other test cases
        self.logger.handlers = []

    
    @patch('requests.get')
    def test_fetch_user_gists_successful_response(self, mock_get):
        # Mock the requests.get function and its return value
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'gist_id': '123', 'description': 'Test Gist'}]

        mock_get.return_value = mock_response

        # Call the fetch_user_gists function
        gists = fetch_user_gists('test_user')
        # Assert that the function returns the expected result
        self.assertEqual(gists, [{'gist_id': '123', 'description': 'Test Gist'}])

    @patch('requests.get')
    def test_fetch_user_gists_error_response(self, mock_get):
        # Mock the requests.get function and its return value
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = 'Not Found'

        mock_get.return_value = mock_response

        # Call the fetch_user_gists function and expect an exception
        with self.assertRaises(Exception) as context:
            fetch_user_gists('nonexistent_user')

        # Assert that the exception message matches the expected format
        self.assertIn('Error fetching gists:', str(context.exception))

    def test_run_fetch_user_gists_none_userr(self):
         # Use a context manager to capture log messages
        with self.assertLogs(self.logger, level='ERROR') as cm:
            # Call the main function with an empty username (mocked input)
            run_fetch_user_gists("")

        # Check that the expected error message is logged
        self.assertEqual(cm.output, ["ERROR:github_gists:GitHub username is required."])

    @patch('requests.get')
    def test_fetch_user_gists_multiple_gists(self, mock_get):
        # Define a mock response for a user with multiple gists
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'description': 'Gist 1',
                'html_url': 'https://gist.github.com/user/gist1',
                'created_at': '2023-10-05T10:00:00Z'  # Add the 'created_at' field
            },
            {
                'description': 'Gist 2',
                'html_url': 'https://gist.github.com/user/gist2',
                'created_at': '2023-10-06T11:00:00Z'
            },
            {
                'description': 'Gist 3',
                'html_url': 'https://gist.github.com/user/gist3',
                'created_at': '2023-10-07T12:00:00Z'
            }
        ]

        # Set up the mock for the requests.get function
        mock_get.return_value = mock_response

        # Call the fetch_user_gists function
        gists = fetch_user_gists('test_user')

        # Assert that the function returns the expected result with 'creation_date'
        expected_gists = [
            {
                'description': 'Gist 1',
                'html_url': 'https://gist.github.com/user/gist1',
                'created_at': '2023-10-05T10:00:00Z'
            },
            {
                'description': 'Gist 2',
                'html_url': 'https://gist.github.com/user/gist2',
                'created_at': '2023-10-06T11:00:00Z'
            },
            {
                'description': 'Gist 3',
                'html_url': 'https://gist.github.com/user/gist3',
                'created_at': '2023-10-07T12:00:00Z'
            }
        ]
        self.assertEqual(gists, expected_gists)



if __name__ == '__main__':
    unittest.main()