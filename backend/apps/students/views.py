from rest_framework import generics, filters
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StudentList(generics.ListAPIView):
    # Get ALL Students
    queryset = Student.objects.order_by('-created_at')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields =
    # search_fields =


class StudentAdd(generics.CreateAPIView):
    # Get Add Students
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    # Get Update Students
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
