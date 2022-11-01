from django.urls import path, include
from .views import RegisterView #, ListUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view(), name="register"),
    # path('list/', ListUserView.as_view(), name="list"),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
