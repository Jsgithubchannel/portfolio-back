from .models import Project
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

class ProjectSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Project
        fields = ['id','title','start_date','end_date','desc','qualifications','achievements','created_at','updated_at','photo']
        read_only_fields = ['id']