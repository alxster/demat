from django.contrib import admin
from .models import TipoCostruzione, Fascicolo, TipoDocumento, Documento, Subalterno, Pratica


@admin.register(TipoCostruzione)
class TipoCostruzioneAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome')


@admin.register(Fascicolo)
class FascicoloAdmin(admin.ModelAdmin):
    list_display = ('foglio', 'particella', 'indirizzo', 'costruttore')
    search_fields = ('costruttore',)


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome')


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'numero', 'data', 'approvato')
    list_filter = ('approvato',)


@admin.register(Subalterno)
class SubalternoAdmin(admin.ModelAdmin):
    list_display = ('fascicolo', 'sub', 'note')


@admin.register(Pratica)
class PraticaAdmin(admin.ModelAdmin):
    list_display = ('note', )
