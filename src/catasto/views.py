from rest_framework import viewsets
from .models import Fascicolo, Documento, TipoCostruzione, TipoDocumento, Pratica, Subalterno
from .serializers import (
    FascicoloSerializer,
    DocumentoSerializer,
    TipoCostruzioneSerializer,
    TipoDocumentoSerializer,
    PraticaSerializer,
    SubalternoSerializer,
)


class TipoCostruzioneViewSet(viewsets.ModelViewSet):
    queryset = TipoCostruzione.objects.all()
    serializer_class = TipoCostruzioneSerializer


class FascicoloViewSet(viewsets.ModelViewSet):
    queryset = Fascicolo.objects.all()
    serializer_class = FascicoloSerializer


class SubalternoViewSet(viewsets.ModelViewSet):
    queryset = Subalterno.objects.all()
    serializer_class = SubalternoSerializer


class PraticaViewSet(viewsets.ModelViewSet):
    queryset = Pratica.objects.all()
    serializer_class = PraticaSerializer


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer