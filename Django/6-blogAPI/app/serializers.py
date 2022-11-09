from rest_framework import serializers
from rest_framework.response import Response
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['title', 'body', 'created', 'owner']   


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment_detail',lookup_field ='pk')

    class Meta:
        model = Post
        fields = ['title', 'body', 'created', 'updated', 'owner', 'comment_set']   


class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.HyperlinkedRelatedField(view_name='comment_detail', read_only=True, lookup_field='pk')
    post = serializers.HyperlinkedIdentityField(view_name='post_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['post', 'owner', 'body', 'created', 'updated']

