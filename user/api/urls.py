from django.urls import path
from user.api import views

app_name = 'blog'

urlpatterns = [
    # path('', views.UserCollection.as_view()),
    path('fans/', views.FanCollection.as_view()),
    path('talents', views.TalentCollection.as_view()),
    
]