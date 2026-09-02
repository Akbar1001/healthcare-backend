from rest_framework import serializers

from doctors.models import Doctor
from patients.models import Patient

from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all()
    )

    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all()
    )

    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id",
            "patient",
            "doctor",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate(self, attrs):
        request = self.context["request"]
        patient = attrs["patient"]

        if patient.created_by != request.user:
            raise serializers.ValidationError(
                "You can only assign doctors to your own patients."
            )

        return attrs