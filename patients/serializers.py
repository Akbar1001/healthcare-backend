from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(
        source="created_by.id"
    )

    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "phone",
            "address",
            "medical_history",
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

    def validate_age(self, value):
        if value > 120:
            raise serializers.ValidationError(
                "Age must be 120 or below."
            )

        return value

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