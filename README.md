# Math API

This is a Python API that performs simple mathematical operations such as addition, subtraction, multiplication, and division.

## Usage

The API is accessed via HTTP POST method at the endpoint `http://localhost:8000/api/`. Make sure the server is running locally.

## DOCUMENTATION

You can acess the docs files with this link: `http://localhost:8000/api/docs`

## Request

Send a POST request to the `http://localhost:8000/api/` endpoint with the following parameters:

- `number1`: The first number for the calculation (integer)
- `number2`: The second number for the calculation (integer)
- `operation`: The operation to be performed (string). Valid options: 'sum' (or '+'), 'subtraction' (or '-'), 'multiplication' (or 'x' or '*'), 'division' (or '/')

Example request using Python:

```bash
import requests

url = 'http://localhost:8000/api/'
data = {"number1" : 100, "number2": 50, "operation": '+'}

req = requests.post(url, data=data)
```


### Response

The API returns a JSON response containing the calculation result or an error message if the operation is invalid.

Example response for a valid request:
{
  "result": 15
}

Example response for a request with an invalid operation:
{
  "error": "INVALID OPERATION"
}

Dependencies
```bash
pip install -r requirements.txt
```

### Execution

Ensure that the server is running and accessible at http://localhost:8000/. Then, make requests to http://localhost:8000/api/ as described above.
```bash
python manage.py runserver
```

### Tests

The tests are located in the folder djangoapi/api/tests
