from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_post(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file_content')
        if files:
            request.data.pop('file_content')

            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                post_qs = Posts.objects.get(id=serializer.data['id'])
                uploaded_files = []
                for file in files:
                    content = ImgFile.objects.create(media=file)
                    uploaded_files.append(content)

                post_qs.file_content.add(*uploaded_files)
                context = serializer.data
                context["file_content"] = [file.id for file in uploaded_files]
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()         
                context = serializer.data            
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
