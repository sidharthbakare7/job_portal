from rest_framework import serializers
from .models import job_seeker,company,post_jobs,apply_job

class job_seekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_seeker
        fields = "__all__"

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = "__all__"

class post_jobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_jobs
        fields = "__all__"

class apply_jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = apply_job
        fields = "__all__"