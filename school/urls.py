from django.urls import path
from school.views import SchoolViewSet

urlpatterns = [
    path('', SchoolViewSet.as_view({'get':'list'})),
    path('<int:pk>', SchoolViewSet.as_view({'get':'retrieve'})),
]