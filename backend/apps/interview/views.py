from rest_framework import generics, filters
from .models import Interview
from .serializers import InterviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class InterviewList(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields =
    # search_fields =


class InterviewAdd(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class InterviewUpdate(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
