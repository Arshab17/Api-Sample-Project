from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Article
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

def first(request):
    return HttpResponse('hello world')


def second (request):
    return JsonResponse(
        {
            'name': 'Arshab',
            'place':'Calicut',
            'true_value':True,
            'none_value':None
        }
    )
@api_view(['GET'])
def blog_details(request,id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(
        serializer.data
        # {
        #     'id':article.id,
        #     'title':article.title,
        #     'content':article.content,
        #     'image':article.image.url,
        #     'created':article.created
        # }
    )
@api_view(['POST'])
def blog_add(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message': 'Blog added successfully'
            }
        )

@api_view(['GET'])
def blog_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles,many=True)# many= true can list the complete items in the model object.
    return Response(
        serializer.data
    )

@api_view(['PUT'])
def blog_update(request,id):
    blog = Article.objects.get(id = id)
    serializer = ArticleSerializer(blog, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
            'message' : 'Blog updated successfully',
            'data' : serializer.data
            }
        )
    return Response(
        serializer.errors
    )

@api_view(['DELETE'])
def blog_delete(request,id):
    blog = Article.objects.get(id=id)
    blog.delete()
    return Response(
        {
        'message' : 'Article deleted successfully'
        }
    )

class ArticleListAPIView(APIView):
    # perimission_classes = [IsAuthenticated]
   # perimission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        blogs = Article.objects.all()
        serializer = ArticleSerializer(blogs,many= True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                "message" : "post created successfully"
                }
            )
        return Response(
            serializer.errors
        )
    
class ArticleApiView(APIView):

    def get(self,request,id):
        blogs = Article.objects.get(id = id)
        serializer = ArticleSerializer(blogs)
        return Response(
            serializer.data
        )

    def put(self,request,id):
        blogs = Article.objects.get(id = id)
        serializer = ArticleSerializer(blogs,data = request.data) 
        if serializer.is_valid():
            serializer.save() 
            return Response(
                {
                "message" : "updated successfully"
                }
            )
        return Response(
            serializer.errors
        ) 
    
    def delete(self,request,id):
        blog = Article.objects.get(id=id)
        blog.delete()
        return Response(
        {
        'message' : 'Article deleted successfully'
        }
    )

class NewArticleList(ListCreateAPIView):
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer   

class NewArticleAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    Lookup_field = "id"



class CommentView(APIView) :
    def get(self,request,id):
        blog = Article.objects.get(id=id)
        comments = Comment.objects.filter(article=blog)
        serializer = CommentSerializer(comments,many=True)
        return Response(
            serializer.data
        )   
    

    def post(self,request,id):
        blog = Article.objects.get(id = id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(article = blog)
            return Response(
                {
                'message' : 'Comment posted successfully'
                }
            )
        return Response(
            serializer.errors
        )