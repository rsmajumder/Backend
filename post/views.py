from pickle import GET
from rest_framework import generics

from .models import * 
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class Post(generics.GenericAPIView):
    serializer_class = PostSerializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("Error")
        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Post successfully Posted',
                'data': []
            }
        return Response(response)
        

        
class Share(generics.GenericAPIView):
    serializer_class = ShareSerializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("Error")
        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'This Post Shared Successfully',
                'data': []
            }
        return Response(response)


# FOR UPLOADING REEL
class Reels(generics.GenericAPIView) :
    serializer_class = reelsSerializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("Error")
        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Story posted successfully',
                'data': []
            }
        return Response(response)


from django.shortcuts import render

# FOR EXPLORING REELS
class view_reels(generics.GenericAPIView) :
    @csrf_exempt
    def reels(request):
        profile = Profile.objects.get(user=request.user)
        profileimage = profile.profile_picture.url
        reels = Reels.objects.all()
        return render(request,{'reels':reels,'profileimage':profileimage})

# FOR LIKING THE REEL
class like_reels(generics.GenericAPIView) :
    @csrf_exempt
    def like_reel(request,id):
        reel = Reels.objects.get(id=id)
        if request.user in reel.likes.all():
            reel.likes.remove(request.user)
        else:
            reel.likes.add(request.user)



# FOR UPLOADING Story
class Story(generics.GenericAPIView) :
    serializer_class = StorySerializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("Error")
        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Story posted successfully',
                'data': []
            }
        return Response(response)

# FOR UPLOADING COMMENT
class Comment(generics.GenericAPIView):
    serializer_class= CommentSerializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("Error")
        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Post successfully Posted',
                'data': []
            }
        return Response(response)

# FOR LIKING THE POST
class like_post(generics.GenericAPIView) :
    @csrf_exempt
    def like_post(request,id):
        post = Post.objects.get(id=id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)