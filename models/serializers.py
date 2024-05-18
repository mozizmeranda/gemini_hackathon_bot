from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, **validated_data):
        instance = self.Meta.model(validated_data)
        instance.save()
        return instance


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer().read_only
    image = serializers.ImageField(required=False)

    class Meta:
        model = Doctor
        fields = ["user", "id", "surname", "name", "specialization", "start_time_of_work", "end_time_of_work", "experience_years", "grafik", "image"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title ', 'created_at']


class DiseaseSerializer(serializers.ModelSerializer):
    user = UserSerializer().read_only

    class Meta:
        model = Disease
        fields = "__all__"
