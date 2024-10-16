import django_filters
from .models import Livre, Auteur

class LivreFilter(django_filters.FilterSet):
    class Meta:
        model = Livre
        fields = {
            'titre': ['exact', 'icontains'],  # Filtre par titre (exact ou contenant une chaîne)
            'date_de_publication': ['exact', 'year__gte'],  # Filtre par année de publication (plus grande ou égale)
        }

class AuteurFilter(django_filters.FilterSet):
    class Meta:
        model = Auteur
        fields = {
            'nom': ['exact', 'icontains'],  # Filtrer par nom
            'nationalite': ['exact'],  # Filtrer par nationalité
        }
