from django.db import models
from django.conf import settings
from guardian.mixins import GuardianUserMixin
from guardian.shortcuts import assign_perm

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    date_de_naissance = models.DateField()
    date_de_deces = models.DateField(null=True, blank=True)
    nationalite = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_auteurs/', null=True, blank=True)
    class Meta:
        permissions = [
            ('voir_auteur', 'Peut voir un auteur'),
            ('changer_auteur', 'Peut modifier un auteur'),
            ('supp_auteur', 'Peut supprimer un auteur'),
        ]

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom
    
class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField(null=True, blank=True)
    email_contact = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='logos_editeurs/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    date_de_publication = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    nombre_de_pages = models.IntegerField()
    langue = models.CharField(max_length=100)
    image_de_couverture = models.ImageField(upload_to='couvertures_livres/', null=True, blank=True)
    format = models.CharField(max_length=50, choices=[('Broché', 'Broché'), ('Relié', 'Relié'), ('Numérique', 'Numérique')])

    # Relation OneToMany avec Catégorie et Editeur
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='livres')

    # Relation ManyToMany avec les Auteurs
    auteurs = models.ManyToManyField(Auteur, related_name='livres')

    class Meta:
        permissions = [
            ('voir_livre', 'Peut voir un livre'),
            ('changer_livre', 'Peut modifier un livre'),
            ('supp_livre', 'Peut supprimer un livre'),
        ]

    def __str__(self):
        return self.titre

class Exemplaire(models.Model):
    etat = models.CharField(max_length=50, choices=[('Neuf', 'Neuf'), ('Bon', 'Bon'), ('Acceptable', 'Acceptable')])
    date_acquisition = models.DateField()
    localisation = models.CharField(max_length=255)
    disponibilite = models.BooleanField(default=True)

    # Relation OneToMany avec Livre
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='exemplaires')

    def __str__(self):
        return f"{self.livre.titre} - {self.etat}"

class Emprunt(models.Model):
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prevue = models.DateTimeField()
    date_retour_effective = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En retard', 'En retard')])
    remarques = models.TextField(null=True, blank=True)

    # Relation ManyToMany avec Exemplaire et Utilisateur
    exemplaire = models.ManyToManyField(Exemplaire, related_name='emprunts')
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='emprunts')

    def __str__(self):
        return f"Emprunt de {self.utilisateur} - {self.statut}"

class Commentaire(models.Model):
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    note = models.IntegerField(default=1)
    visible = models.BooleanField(default=True)
    modéré = models.BooleanField(default=False)

    # Relation OneToMany vers Livre et Utilisateur
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='commentaires')
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commentaires')

    def __str__(self):
        return f"Commentaire de {self.utilisateur} sur {self.livre.titre}"

class Evaluation(models.Model):
    note = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    commentaire = models.TextField(null=True, blank=True)
    date_évaluation = models.DateTimeField(auto_now_add=True)
    recommandé = models.BooleanField(default=False)
    titre = models.CharField(max_length=255)

    # Relation ManyToMany avec Livre et Utilisateur
    livre = models.ManyToManyField(Livre, related_name='evaluations')
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='evaluations')

    def __str__(self):
        return f"Évaluation de {self.utilisateur} pour {self.livre.titre}"

