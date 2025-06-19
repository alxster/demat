from django.contrib import admin
from .models import TipoCostruzione, Fascicolo, TipoDocumento, Documento, Subalterno, Pratica


class DocumentiInlineFascicolo(admin.TabularInline):
    model = Documento.fascicoli.through
    extra = 1


class SubalterniInlineFascicolo(admin.TabularInline):
    model = Subalterno
    extra = 1


class PraticheInlineFascicolo(admin.TabularInline):
    model = Pratica
    extra = 1


class DocumentiInlineSubalterno(admin.TabularInline):
    model = Documento.subalterni.through
    extra = 1


class PraticheInlineSubalterno(admin.TabularInline):
    model = Pratica
    extra = 1


class DocumentiInlinePratica(admin.TabularInline):
    model = Documento.pratiche.through
    extra = 1


@admin.register(TipoCostruzione)
class TipoCostruzioneAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome')


@admin.register(Fascicolo)
class FascicoloAdmin(admin.ModelAdmin):
    list_display = ('foglio', 'particella', 'indirizzo', 'costruttore')
    search_fields = ('costruttore',)
    inlines = (SubalterniInlineFascicolo, PraticheInlineFascicolo, DocumentiInlineFascicolo)


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
    inlines = (PraticheInlineSubalterno, DocumentiInlineSubalterno)


@admin.register(Pratica)
class PraticaAdmin(admin.ModelAdmin):
    list_display = ('fascicolo', 'subalterno', 'note')
    list_filter = ('fascicolo',)
    search_fields = ('note',)
    inlines = (DocumentiInlinePratica,)
