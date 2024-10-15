from django.contrib import admin
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation

admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Categorie)
admin.site.register(Exemplaire)
admin.site.register(Emprunt)
admin.site.register(Commentaire)
admin.site.register(Editeur)
admin.site.register(Evaluation)

# @admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nationalité', 'date_de_naissance', 'date_de_décès')
    search_fields = ('nom', 'nationalité')
    list_filter = ('nationalité',)
    
# @admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_de_publication', 'isbn', 'nombre_de_pages', 'langue', 'categorie')
    search_fields = ('titre', 'isbn', 'langue')
    list_filter = ('date_de_publication', 'categorie', 'langue')
    filter_horizontal = ('auteurs',)  # Pour gérer la relation ManyToMany avec les auteurs
    
# @admin.register(Exemplaire)
class ExemplaireAdmin(admin.ModelAdmin):
    list_display = ('livre', 'etat', 'localisation', 'disponibilite', 'date_acquisition')
    list_filter = ('etat', 'localisation', 'disponibilite')
    search_fields = ('livre__titre',)
    
# @admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('exemplaire', 'utilisateur', 'date_emprunt', 'date_retour_prevue', 'statut')
    list_filter = ('statut',)
    search_fields = ('exemplaire__livre__titre', 'utilisateur__username')
    date_hierarchy = 'date_emprunt'
    
# @admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('livre', 'utilisateur', 'note', 'date_publication', 'visible', 'modere')
    list_filter = ('visible', 'modere', 'note')
    search_fields = ('livre__titre', 'utilisateur__username')
    
# @admin.register(Editeur)
class EditeurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'email_contact', 'site_web')
    search_fields = ('nom', 'adresse')
    list_filter = ('nom',)
    
# @admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('livre', 'utilisateur', 'note', 'date_evaluation', 'recommande')
    list_filter = ('note', 'recommande')
    search_fields = ('livre__titre', 'utilisateur__username')
