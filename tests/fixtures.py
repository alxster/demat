import pytest

from catasto.models import TipoCostruzione, Fascicolo, TipoDocumento, Documento, Subalterno, Pratica


@pytest.fixture
def tipo_costruzione():
    return TipoCostruzione.objects.create(codice="TC01", nome="Costruzione Residenziale")

@pytest.fixture
def fascicolo_data(tipo_costruzione):
    return {
        "foglio": "42",
        "particella": "156",
        "tipo": tipo_costruzione.id,
        "indirizzo": "Via Roma, 1",
        "costruttore": "Costruzioni S.p.A.",
        "note": "Test fascicolo"
    }

@pytest.fixture
def fascicolo(tipo_costruzione):
    return Fascicolo.objects.create(
        foglio="10",
        particella="200",
        tipo=tipo_costruzione,
        indirizzo="Viale Europa, 22",
        costruttore="Edilizia SRL",
        note="Fascicolo di prova"
    )


@pytest.fixture
def tipo_documento():
    return TipoDocumento.objects.create(codice="DOC01", nome="Documento Generico")

@pytest.fixture
def tipo_documento_data():
    return {
        "codice": "DOC01",
        "nome": "Documento Generico"
    }


@pytest.fixture
def documento_data(tipo_documento):
    return {
        "tipo": tipo_documento.id,
        "numero": 1,
        "data": "2023-01-01",
        "approvato": True,
        "note": "Documento di test"
    }

@pytest.fixture
def documento(tipo_documento):
    return Documento.objects.create(
        tipo=tipo_documento, numero=1, data="2023-01-01", approvato=True, note="Documento di prova"
    )


@pytest.fixture
def subalterno_data(fascicolo):
    return {
        "sub": "SUB01",
        "fascicolo": "fascicolo"
    }

@pytest.fixture
def subalterno(fascicolo):
    return Subalterno.objects.create(sub="SUB01", fascicolo=fascicolo)


@pytest.fixture
def pratica_data():
    return {
        "note": "Pratica di prova",
    }

@pytest.fixture
def pratica():
    return Pratica.objects.create(note="Pratica già esistente")
