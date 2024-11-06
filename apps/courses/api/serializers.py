from rest_framework import serializers
from courses.models import Subject, Course, Module, Content

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','title','slug']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order','title','description']

class CourseSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['id','subject','title','slug','overview','created','owner','modules']


class ItemRelatedField(serializers.ModelSerializer):
    def to_representation(self, value):
        return value.render


class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ['order','item']


class ModuleWithContentSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True)
    class Meta:
        model = Module
        fields = ['order','title','description','contents']

class CourseWithContentSerialiser(serializers.ModelSerializer):
    content = ModuleWithContentSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id','subject','title','slug','overview','created','owner','modules']