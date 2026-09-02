from django.urls import path

from .views import (
    MappingListCreateView,
    PatientMappingDetailView,
)


urlpatterns = [
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),

    path(
        "<int:patient_id>/",
        PatientMappingDetailView.as_view(),
        name="patient-mapping-detail",
    ),
]