from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegisterSerializer


@api_view(["POST"])
def logout(request: Request) -> Response:
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)
    return Response({"Message": "You are not logged in"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_register_view(request: Request) -> Response:
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Account has been created'
            data['username'] = account.username  # type: ignore
            data['email'] = account.email  # type: ignore

            refresh = RefreshToken.for_user(account)  # type: ignore
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)  # type: ignore
            }
        else:
            data = serializer.errors
        return Response(data)
    return Response({"Message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)
