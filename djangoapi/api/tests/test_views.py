from django.test import TestCase, RequestFactory
from api.views import math
import json

class MathViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_sum_operation(self):
        request = self.factory.post('/', {'number1': 2, 'number2': 3, 'operation': 'sum'})
        response = math(request)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content, {'result': 5})

    def test_subtraction_operation(self):
        request = self.factory.post('/', {'number1': 5, 'number2': 2, 'operation': 'subtraction'})
        response = math(request)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content, {'result': 3})

    def test_division_operation(self):
        request = self.factory.post('/', {'number1': 10, 'number2': 2, 'operation': 'division'})
        response = math(request)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content, {'result': 5})

    def test_multiplication_operation(self):
        request = self.factory.post('/', {'number1': 3, 'number2': 4, 'operation': 'multiplication'})
        response = math(request)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content, {'result': 12})

    def test_invalid_operation(self):
        request = self.factory.post('/', {'number1': 2, 'number2': 3, 'operation': 'invalid'})
        response = math(request)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content, {'error': 'INVALID OPERATION'})

    def test_invalid_input(self):
        request = self.factory.post('/', {'number1': 'invalid', 'number2': 3, 'operation': 'sum'})
        response = math(request)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['error'], 'INVALID INPUT')
        
#To run the test you need to be in the folder where manage.py is, after that use the command "python manage.py test"