from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),  # app
    
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False),name='home'),
    
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Navegación API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
