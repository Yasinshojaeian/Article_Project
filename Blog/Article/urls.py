from django.urls import path
from .views import *
app_name = "article"
urlpatterns = [
    path('detail/<int:pk>',detail_view,name='article_detail')
]