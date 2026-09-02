from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(
        source="created_by.id"
    )

    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "phone",
            "email",
            "address",
            "created_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]

    def validate_phone(self, value):
        value = value.strip()

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError(
                "Phone number must be between 10 and 15 digits."
            )

        return value

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Doctor name cannot be empty."
            )

        return value

    def validate_specialization(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Specialization cannot be empty."
            )

        return value