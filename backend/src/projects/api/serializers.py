
from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','project_name', 'investment', 'description','website', 'stage', 'country', 'end_date', 'project_image', 'presentation', 'video', 'papers')

