from rest_framework.exceptions import APIException
from rest_framework import status


class CustomValidation(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "error"
    default_detail = {"error": "One or more packages doesn't exist"}