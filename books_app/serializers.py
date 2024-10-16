from rest_framework import serializers
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ['id', 'nom', 'biographie', 'date_de_naissance', 'date_de_deces', 'nationalite', 'photo']
        extra_kwargs = {
            'nom': {'help_text': 'Nom complet de l\'auteur'},
            'biographie': {'help_text': 'Biographie détaillée de l\'auteur'},
            'date_de_naissance': {'help_text': 'Date de naissance de l\'auteur (AAAA-MM-JJ)'},
            'date_de_décès': {'help_text': 'Date de décès de l\'auteur si applicable (optionnel)'},
            'nationalité': {'help_text': 'Nationalité de l\'auteur'},
            'photo': {'help_text': 'photo de l\'auteur'}
        }

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description', 'slug']
        extra_kwargs = {
            'nom': {'help_text': 'nom du livre'},
            'description': {'help_text': ' Description de la catégorie'},
            'slug': {'help_text': 'slug de la catégorie'}
        }

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = ['id', 'nom', 'adresse', 'site_web', 'email_contact', 'description', 'logo']
        extra_kwargs = {
            'nom': {'help_text': 'Nom complet de l\'editeur'},
            'adresse': {'help_text': 'Adresse de l\'editeur'},
            'site_web': {'help_text': 'Site_web de l\'editeur'},
            'email_contact': {'help_text': 'Email_contact de l\'editeur si applicable (optionnel)'},
            'description': {'help_text': 'Description biographique de l\'editeur'},
            'logo': {'help_text': 'logo de l\'editeur'}
        }

class LivreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livre
        fields = [
            'url', 
            'titre', 
            'resume', 
            'date_de_publication', 
            'isbn', 
            'nombre_de_pages', 
            'langue', 
            'image_de_couverture', 
            'format', 
            'auteurs', 
            'categorie', 
            'editeur'
        ]
        extra_kwargs = {
            'titre': {'help_text': 'Titre du livre'},
            'description': {'help_text': 'Résumé ou description du livre'},
            'isbn': {'help_text': 'Numéro ISBN unique du livre'}
        }

class ExemplaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)  # Sérialiseur imbriqué pour le livre

    class Meta:
        model = Exemplaire
        fields = ['id', 'etat', 'date_acquisition', 'localisation', 'disponibilite', 'livre']

class EmpruntSerializer(serializers.ModelSerializer):
    exemplaire = ExemplaireSerializer(many=True, read_only=True)  # Sérialiseur pour les exemplaires
    utilisateur = serializers.StringRelatedField(read_only=True)  # Utilisateur lié

    class Meta:
        model = Emprunt
        fields = ['id', 'date_emprunt', 'date_retour_prevue', 'date_retour_effective', 'statut', 
                  'remarques', 'exemplaire', 'utilisateur']

class CommentaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)  # Sérialiseur imbriqué pour le livre
    utilisateur = serializers.StringRelatedField(read_only=True)  # Utilisateur lié

    class Meta:
        model = Commentaire
        fields = ['id', 'contenu', 'date_publication', 'note', 'visible', 'modéré', 'livre', 'utilisateur']

class EvaluationSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(many=True, read_only=True)  # Sérialiseur pour les livres
    utilisateur = serializers.StringRelatedField(read_only=True)  # Utilisateur lié

    class Meta:
        model = Evaluation
        fields = ['id', 'note', 'commentaire', 'date_évaluation', 'recommandé', 'titre', 'livre', 'utilisateur']
