import requests  # Import the requests library for making HTTP requests
import json  # Import the json library for handling JSON data
import pytest  # Import pytest for testing

# Define the base URL for the GitHub API
BASE_URL = "https://api.github.com"

# Define the GitHub username and personal access token for authentication
GITHUB_USER = "YOUR_GITHUB_USER_NAME"  # Replace with your GitHub username
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your personal access token

# Fixture to provide the base URL and headers for the tests
@pytest.fixture(scope="module")
def github_api():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}  # Set the headers for authentication
    return BASE_URL, headers  # Return the base URL and headers as a tuple

# Utility function to print all response headers in a readable format
def print_response_headers(response):
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")  # Print each header and its value

# Utility function to print the response body in a readable format
def print_response_body(response):
    print("Response Body:")
    print(json.dumps(response.json(), indent=4))  # Pretty-print the JSON response

# Parametrized test function to verify the retrieval of repositories for a specific GitHub user
@pytest.mark.parametrize("username", [GITHUB_USER])
def test_get_repositories_for_user(github_api, username):
    base_url, headers = github_api  # Unpack the base URL and headers from the fixture

    # Make a GET request to fetch repositories for the specified user
    response = requests.get(f"{base_url}/users/{username}/repos", headers=headers)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response content type is JSON
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    # Parse the response body as JSON
    body = response.json()

    # Assert that the response body is not an empty array
    assert len(body) > 0

    # Assert that the first repository's name is not null
    assert body[0]['name'] is not None

    # Assert that the first repository's ID is greater than 0
    assert body[0]['id'] > 0

    # Assert that the owner's login matches the specified user
    assert body[0]['owner']['login'] == username

    # Print the response headers and body in a readable format
    print_response_headers(response)
    print_response_body(response)
