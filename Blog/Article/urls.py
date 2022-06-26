from django.urls import path
from .views import *

app_name = "article"
urlpatterns = [
    path('detail/<int:pk>',detail,name='article_detail'),
    # path('detail/<int:pk>',ArticlesDetailView.as_view(),name='article_detail')
]