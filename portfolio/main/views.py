from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.filter(pk=pk)
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, many=True)
        
        return Response(serializer.data)