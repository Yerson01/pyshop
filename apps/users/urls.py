from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('', include('djoser.urls')),
    path('jwt', include('djoser.urls.jwt'))
]