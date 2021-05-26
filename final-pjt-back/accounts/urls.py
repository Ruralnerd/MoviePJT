from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('profile_detail/', views.profile_detail, name='profile_detail'),    
    path('api-token-auth/', obtain_jwt_token),
]