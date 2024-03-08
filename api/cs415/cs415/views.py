from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication
from cs415.models import User, UserAddress, DriverLicense, Vehicle, ParkingInfo
from cs415.serializers import (
    UserSerializer,
    UserAddressSerializer,
    DriverLicenseSerializer,
    ParkingInfoSerializer,
    VehicleSerializer,
)


class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})


class GetSingleUserAPIView(APIView):
    def get(self, request, id):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)

        return Response({"user": serializer.data})


class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {
                    "success": False,
                    "error": "Email OR Username and Password must have a value",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response(
                {"success": False, "error": "User with this email does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        check_pass = User.objects.filter(email=email, pass_word=password).exists()
        if check_pass == False:
            return Response(
                {"success": False, "error": "Incorrect password for user"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        user = User.objects.get(email=email, pass_word=password)
        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {"token": jwt_token}
            return Response(
                {"success": True, "token": jwt_token}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"success": False, "error": "Invalid Login Credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserAddressAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        addresses = UserAddress.objects.all()
        serializer = UserAddressSerializer(addresses, many=True)
        return Response({"addresses": serializer.data})


class DriverLicenseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        serializer = DriverLicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        licenses = DriverLicense.objects.all()
        serializer = DriverLicenseSerializer(licenses, many=True)
        return Response({"Driver licenses": serializer.data})


class VehicleAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        Vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(Vehicles, many=True)
        return Response({"Vehicles": serializer.data})


class GetSingleVehicleAPIView(APIView):
    def get(self, request, id):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        vehicle = Vehicle.objects.get(pk=id)
        serializer = VehicleSerializer(vehicle)
        return Response({"vehicle": serializer.data})


class ParkingInfoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        serializer = ParkingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        if JWT_AUTH:
            JWTAuthentication.authenticate(self, request=request)
        Parking_number = ParkingInfo.objects.all()
        serializer = ParkingInfoSerializer(Parking_number, many=True)
        return Response({"Parking Location": serializer.data})
