from rest_framework import serializers
from .models import Id, Studentarr
from rest_framework.renderers import JSONRenderer

class IdSerializer(serializers.ModelSerializer):

    #snipping = serializers.StringRelatedField(many=True)

    class Meta:
        model = Id
        #fields = ['id', 'name', 'last_name', 'age', 'array_of_fields_student']
        fields = ['i_d', 'first_name', 'last_name']
        #fields = "__all__"

    #def get_snipping(self, obj):
    #    return (obj.id)

class StudentarrSerializer(serializers.ModelSerializer):
    #snipping = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Studentarr
        fields = ['i_d', 'name', 'grade', 'student_details']

'''
class StudentarrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studentarr
        fields = ['i','n','g']
'''
