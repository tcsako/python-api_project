import requests  # Import the requests library for making HTTP requests
import json  # Import the json library for handling JSON data
import pytest  # Import pytest for testing

# Define the base URL for the JSONPlaceholder API
BASE_URL = "http://jsonplaceholder.typicode.com"

# Fixture to provide the base URL
@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

# Utility function to print all response headers in a readable format
def print_response_headers(response):
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

# Utility function to print the response body in a readable format
def print_response_body(response):
    print("Response Body:")
    print(json.dumps(response.json(), indent=4))

# Parametrized test function to verify the retrieval of a post by ID
@pytest.mark.parametrize("post_id, expected_title", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
    (2, "qui est esse"),
    (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut")
])
def test_get_post_by_id(base_url, post_id, expected_title):
    response = requests.get(f"{base_url}/posts/{post_id}")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response content type is JSON
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    # Parse the response body as JSON
    body = response.json()

    # Assert that the post ID matches the expected ID
    assert body['id'] == post_id

    # Assert that the post title matches the expected title
    assert body['title'] == expected_title

    # Assert that the post body is not null
    assert body['body'] is not None

    # Assert that the user ID is greater than 0
    assert body['userId'] > 0

    # Print the response headers and body in a readable format
    print_response_headers(response)
    print_response_body(response)

# Test function to verify the creation of a new post
def test_create_post(base_url):
    # Define the new post data as a dictionary
    new_post = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    # Make a POST request to create a new post
    response = requests.post(f"{base_url}/posts", json=new_post)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Parse the response body as JSON
    body = response.json()

    # Assert that the post title matches the expected title
    assert body['title'] == new_post['title']

    # Assert that the post body matches the expected body
    assert body['body'] == new_post['body']

    # Assert that the user ID matches the expected user ID
    assert body['userId'] == new_post['userId']

    # Assert that the post ID is greater than 0
    assert body['id'] > 0

    # Print the response headers and body in a readable format
    print_response_headers(response)
    print_response_body(response)

# Test function to verify the update of an existing post
def test_update_post(base_url):
    # Define the updated post data as a dictionary
    updated_post = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }

    # Make a PUT request to update the existing post
    response = requests.put(f"{base_url}/posts/1", json=updated_post)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the response body as JSON
    body = response.json()

    # Assert that the post title matches the updated title
    assert body == updated_post

    # Print the response headers and body in a readable format
    print_response_headers(response)
    print_response_body(response)

# Test function to verify the partial update of an existing post
def test_patch_post(base_url):
    # Define the partial update data as a dictionary
    partial_update = {
        "title": "patched title"
    }

    # Make a PATCH request to partially update the existing post
    response = requests.patch(f"{base_url}/posts/1", json=partial_update)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the response body as JSON
    body = response.json()

    # Assert that the post title matches the patched title
    assert body['title'] == partial_update['title']

    # Assert that the post ID is 1
    assert body['id'] == 1

    # Assert that the user ID is greater than 0
    assert body['userId'] > 0

    # Print the response headers and body in a readable format
    print_response_headers(response)
    print_response_body(response)

# Test function to verify the deletion of an existing post
def test_delete_post(base_url):
    # Make a DELETE request to delete the existing post
    response = requests.delete(f"{base_url}/posts/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Print the response headers and body in a readable format
    print_response_headers(response)
    print_response_body(response)

# Test function to verify the HEAD request for an existing post
def test_head_post(base_url):
    # Make a HEAD request to get headers for the existing post
    response = requests.head(f"{base_url}/posts/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the Content-Type header contains "application/json"
    assert 'application/json' in response.headers['Content-Type']

    # Print the response headers in a readable format
    print_response_headers(response)
