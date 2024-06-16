from rest_framework import serializers

from .models import Student, Fellows_table

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'addr', 'phone')

class FellowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fellows_table
        fields = '__all__'