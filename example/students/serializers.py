from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return {
            'name': obj.name,
            'surname': obj.surname,
            'age': obj.age,
        }

    class Meta:
        model = Student
        fields = ['name', 'surname', 'age']


