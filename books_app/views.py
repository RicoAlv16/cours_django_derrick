from django.shortcuts import render
from rest_framework import viewsets
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation
from .serializers import AuteurSerializer, LivreSerializer, CategorieSerializer, ExemplaireSerializer, EmpruntSerializer, CommentaireSerializer, EditeurSerializer, EvaluationSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import LivreFilter, AuteurFilter

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

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
