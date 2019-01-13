from rest_framework import serializers
from .models import FPhoto, FGroup

class FPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FPhoto
        fields = '__all__'

class FPhotoIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = FPhoto
        fields = ['id']



class FGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = FGroup
        fields = '__all__'