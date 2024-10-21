"""
URL configuration for cours_django_derrick project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import AuteurListView, AuteurViewSet, LivreListView, LivreViewSet, CategorieViewSet, ExemplaireViewSet, CommentaireViewSet, EditeurViewSet, EvaluationViewSet, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Book API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from rest_framework_simplejwt.views import TokenBlacklistView
from two_factor.urls import urlpatterns as tf_urls




urlpatterns = [
    path("admin/", admin.site.urls),
]

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'exemplaire', ExemplaireViewSet)
router.register(r'commentaire', CommentaireViewSet)
router.register(r'editeur', EditeurViewSet)
router.register(r'evaluation', EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Endpoint pour obtenir le token d'accès et de rafraîchissement
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Endpoint pour blacklister un token lors de la déconnexion
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('', include(tf_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
