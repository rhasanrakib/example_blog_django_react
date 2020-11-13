"""grayspaceit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import posts
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('posts/', include('posts.urls')),
    path('api/auth/', include('api.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    # path('api/token/', jwt_views.TokenObtainSlidingView.as_view()
        #),
    # path('api/token/refresh/', jwt_views.TokenRefreshSlidingView.as_view()
         #),
    # path('api/token/verify/', jwt_views.TokenVerifyView.as_view()
         #),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# from rest_framework_simplejwt.views import (
# TokenObtainSlidingView,
# TokenRefreshSlidingView,
# TokenVerifyView
# )
