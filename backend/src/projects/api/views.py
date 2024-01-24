from rest_framework.generics import ListAPIView, RetrieveAPIView
from projects.models import Project
from .serializers import ProjectSerializer
from rest_framework import permissions

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes =(permissions.AllowAny,)

class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes =(permissions.AllowAny,)

