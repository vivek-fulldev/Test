from django.urls import path
from .views import registeruser,posts
urlpatterns = [
	path('',registeruser),
	path('post/<slug:data>',posts)
]

