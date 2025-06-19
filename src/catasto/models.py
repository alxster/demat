from functools import cached_property

from django.db import models


class TipoCostruzione(models.Model):

    codice = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo Costruzione"
        verbose_name_plural = "Tipi Costruzione"

    def __str__(self):
        return self.nome


class Fascicolo(models.Model):
    foglio = models.CharField(max_length=20)
    particella = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoCostruzione, on_delete=models.CASCADE, blank=True, null=True)
    indirizzo = models.CharField(max_length=100, blank=True, null=True)
    costruttore = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Fascicolo"
        verbose_name_plural = "Fascicoli"

    def __str__(self):
        return f"Foglio: {self.foglio} - Particella: {self.particella}"


class Subalterno(models.Model):
    fascicolo = models.ForeignKey(Fascicolo, on_delete=models.CASCADE)
    sub = models.CharField(max_length=20)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Subalterno"
        verbose_name_plural = "Subalterni"

    def __str__(self):
        return f"{self.fascicolo} - Sub: {self.sub}"


class Pratica(models.Model):
    fascicolo = models.ForeignKey(Fascicolo, on_delete=models.CASCADE, related_name='pratiche')
    subalterno = models.ForeignKey(Subalterno, on_delete=models.CASCADE, null=True, blank=True, related_name='pratiche')
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Pratica"
        verbose_name_plural = "Pratiche"

    def __str__(self):
        sub_info = f" - Sub: {self.subalterno.sub}" if self.subalterno else ""
        return f"{self.fascicolo}{sub_info}"


class TipoDocumento(models.Model):

    codice = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipi Documento"

    def __str__(self):
        return self.nome


def directory_path(instance, filename):
    """
    Create a structured path for file uploads based on document type and date.
    """
    # Get the document type code or use 'misc' if not available
    tipo_code = getattr(instance.tipo, 'codice', 'misc') if instance.tipo else 'misc'

    # Use the current date for organizing files
    from datetime import datetime
    date_path = datetime.now().strftime('%Y/%m/%d')

    # Return a structured path: tipo_code/year/month/day/filename
    return f"{tipo_code}/{date_path}/{filename}"


class Documento(models.Model):

    tipo = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    file = models.FileField(upload_to=directory_path)
    numero = models.IntegerField(blank=True, null=True)
    numero_progressivo = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    approvato = models.BooleanField(default=False)
    data_approvazione = models.DateField(blank=True, null=True)
    numero_protocollo = models.CharField(max_length=10, blank=True, null=True)
    numero_protocollo_generale = models.CharField(max_length=10, blank=True, null=True)
    numero_protocollo_settore = models.CharField(max_length=10, blank=True, null=True)
    note = models.TextField(max_length=1000, blank=True, null=True)
    trascrizione = models.TextField(max_length=10000, blank=True, null=True)
    richiedente = models.CharField(max_length=100, blank=True, null=True)
    destinatario = models.CharField(max_length=100, blank=True, null=True)
    pratiche = models.ManyToManyField(Pratica, blank=True, related_name='documenti')
    subalterni = models.ManyToManyField(Subalterno, blank=True, related_name='documenti')
    fascicoli = models.ManyToManyField(Fascicolo, blank=True, related_name='documenti')

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documenti"

    @cached_property
    def pratica(self):
        return self.pratiche.first()

    def __str__(self):
        return str(self.tipo)
