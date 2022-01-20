from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path ('abc/',views.ham1, name = 'ham'),
    path('', views.index, name = 'index'),
    path('login/', views.regiter,name = 'login'),
    path('ques/',views.list_question,name = "quest"),
    path('choice/<int:quest_id>',views.detailChoice,name= "pchoice"),
    path('<int:quest_id>', views.vote, name = "vote"),
]
