from .models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id','title','start_date','end_date','desc','qualifications','achievements','created_at','updated_at','photo']
        read_only_fields = ['id']