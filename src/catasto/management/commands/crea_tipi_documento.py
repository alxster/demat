from django.core.management.base import BaseCommand

from catasto.data.tipi_documento import TIPO_DOCUMENTO
from catasto.models import TipoDocumento


class Command(BaseCommand):
    help = 'Crea i tipi documento'

    def handle(self, *args, **kwargs):
        for codice, nome in TIPO_DOCUMENTO:
            TipoDocumento.objects.create(codice=codice, nome=nome)

