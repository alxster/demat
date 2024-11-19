from django.db import models


class TipoCostruzione(models.Model):

    codice = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo Costruzione"
        verbose_name_plural = "Tipi Costruzione"


class Fascicolo(models.Model):
    foglio = models.CharField(max_length=20)
    particella = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoCostruzione, on_delete=models.CASCADE, blank=True, null=True)
    indirizzo = models.CharField(max_length=100, blank=True, null=True)
    costruttore = models.CharField(max_length=100, blank=True, null=True)
    pratiche = models.ManyToManyField('Pratica', related_name='fascicoli')
    documenti = models.ManyToManyField('Documento', related_name='fascicoli')
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Fascicolo"
        verbose_name_plural = "Fascicoli"


class Subalterno(models.Model):
    fascicolo = models.ForeignKey(Fascicolo, on_delete=models.CASCADE)
    sub = models.CharField(max_length=20)
    pratiche = models.ManyToManyField('Pratica', related_name='subalterni')
    documenti = models.ManyToManyField('Documento', related_name='subalterni')
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Subalterno"
        verbose_name_plural = "Subalterni"


class Pratica(models.Model):

    documenti = models.ManyToManyField('Documento', related_name='pratiche')
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Pratica"
        verbose_name_plural = "Pratiche"


class TipoDocumento(models.Model):

    codice = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipi Documento"


def directory_path(instance, filename):
    return filename


class Documento(models.Model):

    tipo = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    file = models.FileField(upload_to=directory_path)
    numero = models.IntegerField(blank=True, null=True)
    numero_progressivo = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data_approvazione = models.DateField(blank=True, null=True)
    numero_protocollo = models.CharField(max_length=10, blank=True, null=True)
    numero_protocollo_generale = models.CharField(max_length=10, blank=True, null=True)
    numero_protocollo_settore = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documenti"
