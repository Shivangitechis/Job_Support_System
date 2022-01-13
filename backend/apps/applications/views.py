from rest_framework import generics, filters
from .models import Application, Student
from .serailzers import ApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.order_by('=Created at')
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields =
    # search_fields =


class ApplicationAdd(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
