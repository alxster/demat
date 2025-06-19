from rest_framework import serializers
from .models import Fascicolo, Documento, TipoCostruzione, TipoDocumento, Pratica, Subalterno


class TipoCostruzioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCostruzione
        fields = "__all__"


class FascicoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fascicolo
        fields = "__all__"


class SubalternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subalterno
        fields = "__all__"


class PraticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pratica
        fields = "__all__"


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = "__all__"


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"
        extra_kwargs = {
            'file': {'required': False, 'allow_null': True},
        }