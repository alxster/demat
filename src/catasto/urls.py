from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    FascicoloViewSet,
    DocumentoViewSet,
    TipoCostruzioneViewSet,
    TipoDocumentoViewSet,
    PraticaViewSet,
    SubalternoViewSet,
)

router = DefaultRouter()

# Registriamo i ViewSet con il router
router.register(r'tipi-costruzioni', TipoCostruzioneViewSet, basename='tipo-costruzione')
router.register(r'fascicoli', FascicoloViewSet, basename='fascicolo')
router.register(r'subalterni', SubalternoViewSet, basename='subalterno')
router.register(r'pratiche', PraticaViewSet, basename='pratica')
router.register(r'tipi-documenti', TipoDocumentoViewSet, basename='tipo-documento')
router.register(r'documenti', DocumentoViewSet, basename='documento')

urlpatterns = [
    path("", include(router.urls)),  # Include tutte le rotte generate dal router
]