from django.shortcuts import render
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation
from .serializers import AuteurSerializer, LivreSerializer, CategorieSerializer, ExemplaireSerializer, EmpruntSerializer, CommentaireSerializer, EditeurSerializer, EvaluationSerializer
from rest_framework import generics, viewsets, status
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import LivreFilter, AuteurFilter
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, DjangoObjectPermissions
from guardian.shortcuts import assign_perm

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoObjectPermissions]

    # assigner des permissions à un utilisateur juste après qu'un objet a été créé ou modifié.
    def perform_create(self, serializer):
        auteur = serializer.save()  
        # Assigner la permission view_auteur à l'utilisateur connecté pour ce livre
        assign_perm('voir_auteur', self.request.user, auteur)

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [DjangoModelPermissions]

    # assigner des permissions à un utilisateur juste après qu'un objet a été créé ou modifié.
    def perform_create(self, serializer):
        livre = serializer.save()  
        # Assigner la permission view_livre à l'utilisateur connecté pour ce livre
        assign_perm('voir_livre', self.request.user, livre)

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class LivreListView(generics.ListAPIView):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LivreFilter
    ordering_fields = ['titre', 'date_de_publication']  # Attributs pour trier
    ordering = ['titre']  # Tri par défaut

class AuteurListView(generics.ListAPIView):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AuteurFilter
    ordering_fields = ['nom', 'date_de_naissance']  # Attributs pour trier
    ordering = ['nom']  # Tri par défaut

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklister le token de rafraîchissement
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Seuls les utilisateurs authentifiés peuvent accéder

    def get(self, request):
        return Response(data={"message": "Vous êtes authentifié"}, status=status.HTTP_200_OK)
