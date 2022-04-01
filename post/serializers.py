from rest_framework import serializers
from .models import *

#Create Post Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Share
        fields = '__all__'


class reelsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Reels
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Story
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = '__all__'