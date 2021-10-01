from django.http import response
from django.test import TestCase
import requests
from .services.pypi import request_package_on_pypi


class TestPypiAPI(TestCase):
    def test_request_package(self):
        response = request_package_on_pypi('sampleproject')

        self.assertEqual(200, response.status_code)

    def test_request_package_version(self):
        response = request_package_on_pypi('sampleproject', '2.0.0')

        self.assertEqual(200, response.status_code)
    
    def test_package_dont_exists(self):
        response = request_package_on_pypi('alskdjaslkdj')

        self.assertEqual(404, response.status_code)

    def test_package_version_dont_exists(self):
        response = request_package_on_pypi('sampleproject', '0.0.0')

        self.assertEqual(404, response.status_code)