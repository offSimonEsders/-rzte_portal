import json

from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from appointment.models import Appointment
from appointment.serializer import ReadAppointmentSerializer


# Create your views here.

class AppointmentView(viewsets.ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = ReadAppointmentSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(patient=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.patient != request.user:
            raise PermissionDenied(detail="Sie haben keine Berechtigung, auf diesen Termin zuzugreifen.")
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Antwort zurückgeben
        return Response(serializer.data, status=status.HTTP_201_CREATED)