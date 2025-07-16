from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    Custom exception handler to return JSON responses for exceptions.
    """
    print(f"Exception: {exc}, Context: {context}")

    response = exception_handler(exc, context)

    if response is None:
        # If the default handler did not return a response, create a custom one
        response = Response(
            {'detail': str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
