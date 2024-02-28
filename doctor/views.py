import json

from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from doctor.models import Doctor, specialities_choices, title_choices
from doctor.serializers import DoctorSerializer


# Create your views here.

class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = DoctorSerializer(Doctor.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        loaded_data = json.dumps(request.data)
        loaded_data = json.loads(loaded_data)
        Doctor.objects.create(name=loaded_data['name'], speciality=loaded_data['speciality'],
                              title=loaded_data['title']).save()
        return Response()

    def delete(self, request):
        loaded_data = json.dumps(request.data)
        loaded_data = json.loads(loaded_data)
        if ('id' in loaded_data):
            doctor = Doctor.objects.filter(id=loaded_data['id'])
            if (doctor.exists()):
                doctor.delete()
                return Response({'Doctor is deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'Request failed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Request failed'}, status=status.HTTP_400_BAD_REQUEST)
