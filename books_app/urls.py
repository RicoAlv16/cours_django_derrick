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
from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, LivreViewSet, CategorieViewSet, ExemplaireViewSet, CommentaireViewSet, EditeurViewSet, EvaluationViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
]

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

urlpatterns = [
    path('api/hello/', HelloWorld.as_view(), name='hello_world'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


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
]
