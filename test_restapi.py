import pytest
import requests


@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():  # to verify the parts of the response

    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'
    # Act
    response = requests.get(url)
    body = response.json()
    # This will parse the response data from JSON text into a Python dictionary object which will be useful for
    # validation.
    # Assert
    assert response.status_code == 200  # verify the request was successful
    assert 'Python' in body['AbstractText']  # ths answer shd somewhere has the word ‘python’


# marker name is not needed in new file
