from django.db import models
from django.db.models import fields
from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    running = serializers.BooleanField()