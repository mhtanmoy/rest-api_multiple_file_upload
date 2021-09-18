from rest_framework import serializers
from .models import *




class ImgFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgFile
        fields= '__all__'

class PostSerializer(serializers.ModelSerializer):
    imgfile=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Posts
        fields= '__all__'

    def get_imgfile(self,obj):
        img=obj.imgfile_set.all()
        serializer=ImgFileSerializer(img, many=True)
        return serializer.data
   