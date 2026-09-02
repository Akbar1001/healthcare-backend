from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = (
            PatientDoctorMapping.objects
            .filter(patient__created_by=request.user)
            .select_related("patient", "doctor")
            .order_by("-created_at")
        )

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(
            data=request.data,
            context={"request": request},
        )

        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            mapping = serializer.save()
        except IntegrityError:
            return Response(
                {
                    "error": (
                        "This doctor is already assigned "
                        "to this patient."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        response_serializer = PatientDoctorMappingSerializer(mapping)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )


class PatientMappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = (
            PatientDoctorMapping.objects
            .filter(
                patient_id=patient_id,
                patient__created_by=request.user,
            )
            .select_related("patient", "doctor")
            .order_by("-created_at")
        )

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True,
        )

        return Response(serializer.data)

    def delete(self, request, patient_id):
        mapping = get_object_or_404(
            PatientDoctorMapping,
            pk=patient_id,
            patient__created_by=request.user,
        )

        mapping.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )