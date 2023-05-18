from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import*


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        exclude = ('created',)

        # fields = '__all__'      # to select all object.


class CommentSerializer(ModelSerializer):
    article = serializers.SerializerMethodField()

    def get_article(self,comment):
        blog = comment.article
        serializer = ArticleSerializer(blog)
        return serializer.data
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['article',]
        depth = 3