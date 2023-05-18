from django.urls import path
from .import views

urlpatterns = [
    path('', views.first,name='blog'),
    path("second/",views.second,name='second'),
    path('blog/<int:id>/',views.blog_details,name='blog_details'),
    path('blog_add',views.blog_add,name='blog_add'),
    path('blogs',views.blog_list,name='blogs'),
    path('blog/<int:id>/update',views.blog_update,name='blog_update'),
    path('blog/<int:id>/delete/',views.blog_delete,name="blog_delete"),

    path('class/blog/',views.ArticleListAPIView.as_view()),

    path('class/<int:id>/blog/',views.ArticleApiView.as_view()),

    path('class/article/',views.NewArticleList.as_view()),
    path('new/article/<int:id>/',views.NewArticleList.as_view()),

    path('comments/<int:id>',views.CommentView.as_view(),name='comment_view')
    
]