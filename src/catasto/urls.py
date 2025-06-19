from django.urls import path
from .views import (
    # Template-based views
    # Index
    IndexView,
    # TipoCostruzione
    TipoCostruzioneListView,
    TipoCostruzioneDetailView,
    TipoCostruzioneCreateView,
    TipoCostruzioneUpdateView,
    TipoCostruzioneDeleteView,
    # Fascicolo
    FascicoloListView,
    FascicoloDetailView,
    FascicoloCreateView,
    FascicoloUpdateView,
    FascicoloDeleteView,
    # Subalterno
    SubalternoListView,
    SubalternoDetailView,
    SubalternoCreateView,
    SubalternoUpdateView,
    SubalternoDeleteView,
    # Pratica
    PraticaListView,
    PraticaDetailView,
    PraticaCreateView,
    PraticaUpdateView,
    PraticaDeleteView,
    # TipoDocumento
    TipoDocumentoListView,
    TipoDocumentoDetailView,
    TipoDocumentoCreateView,
    TipoDocumentoUpdateView,
    TipoDocumentoDeleteView,
    # Documento
    DocumentoListView,
    DocumentoDetailView,
    DocumentoCreateView,
    DocumentoUpdateView,
    DocumentoDeleteView,
)

app_name = 'catasto'

# Template-based URLs
template_urlpatterns = [
    # Index URL
    path('', IndexView.as_view(), name='index'),

    # TipoCostruzione URLs
    path('tipi-costruzione/', TipoCostruzioneListView.as_view(), name='tipocostruzione-list'),
    path('tipi-costruzione/<int:pk>/', TipoCostruzioneDetailView.as_view(), name='tipocostruzione-detail'),
    path('tipi-costruzione/create/', TipoCostruzioneCreateView.as_view(), name='tipocostruzione-create'),
    path('tipi-costruzione/<int:pk>/update/', TipoCostruzioneUpdateView.as_view(), name='tipocostruzione-update'),
    path('tipi-costruzione/<int:pk>/delete/', TipoCostruzioneDeleteView.as_view(), name='tipocostruzione-delete'),

    # Fascicolo URLs
    path('fascicoli/', FascicoloListView.as_view(), name='fascicolo-list'),
    path('fascicoli/<int:pk>/', FascicoloDetailView.as_view(), name='fascicolo-detail'),
    path('fascicoli/create/', FascicoloCreateView.as_view(), name='fascicolo-create'),
    path('fascicoli/<int:pk>/update/', FascicoloUpdateView.as_view(), name='fascicolo-update'),
    path('fascicoli/<int:pk>/delete/', FascicoloDeleteView.as_view(), name='fascicolo-delete'),

    # Subalterno URLs
    path('subalterni/', SubalternoListView.as_view(), name='subalterno-list'),
    path('subalterni/<int:pk>/', SubalternoDetailView.as_view(), name='subalterno-detail'),
    path('subalterni/create/', SubalternoCreateView.as_view(), name='subalterno-create'),
    path('subalterni/<int:pk>/update/', SubalternoUpdateView.as_view(), name='subalterno-update'),
    path('subalterni/<int:pk>/delete/', SubalternoDeleteView.as_view(), name='subalterno-delete'),

    # Pratica URLs
    path('pratiche/', PraticaListView.as_view(), name='pratica-list'),
    path('pratiche/<int:pk>/', PraticaDetailView.as_view(), name='pratica-detail'),
    path('pratiche/create/', PraticaCreateView.as_view(), name='pratica-create'),
    path('pratiche/<int:pk>/update/', PraticaUpdateView.as_view(), name='pratica-update'),
    path('pratiche/<int:pk>/delete/', PraticaDeleteView.as_view(), name='pratica-delete'),

    # TipoDocumento URLs
    path('tipi-documento/', TipoDocumentoListView.as_view(), name='tipodocumento-list'),
    path('tipi-documento/<int:pk>/', TipoDocumentoDetailView.as_view(), name='tipodocumento-detail'),
    path('tipi-documento/create/', TipoDocumentoCreateView.as_view(), name='tipodocumento-create'),
    path('tipi-documento/<int:pk>/update/', TipoDocumentoUpdateView.as_view(), name='tipodocumento-update'),
    path('tipi-documento/<int:pk>/delete/', TipoDocumentoDeleteView.as_view(), name='tipodocumento-delete'),

    # Documento URLs
    path('documenti/', DocumentoListView.as_view(), name='documento-list'),
    path('documenti/<int:pk>/', DocumentoDetailView.as_view(), name='documento-detail'),
    path('documenti/create/', DocumentoCreateView.as_view(), name='documento-create'),
    path('documenti/<int:pk>/update/', DocumentoUpdateView.as_view(), name='documento-update'),
    path('documenti/<int:pk>/delete/', DocumentoDeleteView.as_view(), name='documento-delete'),
]

# Use template_urlpatterns as the main urlpatterns
urlpatterns = template_urlpatterns
