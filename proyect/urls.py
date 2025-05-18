from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),  # app


    path('accounts/', include('allauth.urls')),  # LOGIN/LOGOUT WEB
    path('api-auth/', include('rest_framework.urls')),  # Navegación API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
