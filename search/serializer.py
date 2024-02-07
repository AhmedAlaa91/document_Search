from rest_framework import serializers

from .models import Documents


class Documentserializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ["title", "content"]
