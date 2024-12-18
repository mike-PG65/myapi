from rest_framework import serializers
from . models import Mytable

class Myserializer(serializers.ModelSerializer):
    class Meta:
        model = Mytable
        fields = '__all__'