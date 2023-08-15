from django.urls import path
from api_app import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('api/documentation/', views.docs, name='docs'),
    path('api/real-estate-agents-leads/', views.real_estate_agents_leads, name='realestate-lead'),
    path('api/youtube-creators-leads/', views.youtube_creators_leads, name='yt-lead'),
]
