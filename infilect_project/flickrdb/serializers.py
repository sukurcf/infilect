from rest_framework import serializers
from .models import FPhoto

class FPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FPhoto
        fields = '__all__'