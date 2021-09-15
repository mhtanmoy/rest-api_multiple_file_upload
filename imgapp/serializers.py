from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Posts
        fields = ['id', 'texts', 'file_content']
        extra_kwargs = {
            "file_content": {
                "required": False,
            }
        }
    
   