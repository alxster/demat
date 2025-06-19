import pytest
from django.urls import reverse
from rest_framework import status

from .fixtures import *


# ----------------------
# Test TipoCostruzione
# ----------------------

@pytest.mark.django_db
class TestTipoCostruzioneViewSet:

    def test_create_tipo_costruzione(self, client):
        """Test per la creazione di un TipoCostruzione."""
        url = reverse('tipocostruzione-list')
        data = {"codice": "TC02", "nome": "Costruzione Industriale"}
        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert TipoCostruzione.objects.count() == 1
        assert TipoCostruzione.objects.first().nome == "Costruzione Industriale"

    def test_list_tipo_costruzione(self, client, tipo_costruzione):
        """Test per il recupero della lista di Tipi di Costruzione."""
        url = reverse('tipocostruzione-list')
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['nome'] == "Costruzione Residenziale"

    def test_retrieve_tipo_costruzione(self, client, tipo_costruzione):
        """Test per il dettaglio di un singolo TipoCostruzione."""
        url = reverse('tipocostruzione-detail', args=[tipo_costruzione.id])
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['nome'] == "Costruzione Residenziale"

    def test_update_tipo_costruzione(self, client, tipo_costruzione):
        """Test per l'aggiornamento di un TipoCostruzione."""
        url = reverse('tipocostruzione-detail', args=[tipo_costruzione.id])
        updated_data = {"codice": "TC01", "nome": "Costruzione Aggiornata"}
        response = client.patch(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        tipo_costruzione.refresh_from_db()
        assert tipo_costruzione.nome == "Costruzione Aggiornata"

    def test_delete_tipo_costruzione(self, client, tipo_costruzione):
        """Test per l'eliminazione di un TipoCostruzione."""
        url = reverse('tipocostruzione-detail', args=[tipo_costruzione.id])
        response = client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert TipoCostruzione.objects.count() == 0


# ----------------------
# Test Fascicolo
# ----------------------

@pytest.mark.django_db
class TestFascicoloViewSet:

    def test_create_fascicolo(self, client, fascicolo_data):
        """Test per la creazione di un Fascicolo."""
        url = reverse('fascicolo-list')
        response = client.post(url, fascicolo_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Fascicolo.objects.count() == 1
        assert Fascicolo.objects.first().foglio == "42"

    def test_list_fascicoli(self, client, fascicolo):
        """Test per il recupero della lista di Fascicoli."""
        url = reverse('fascicolo-list')
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['foglio'] == fascicolo.foglio

    def test_retrieve_fascicolo(self, client, fascicolo):
        """Test per il dettaglio di un singolo Fascicolo."""
        url = reverse('fascicolo-detail', args=[fascicolo.id])
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['foglio'] == fascicolo.foglio

    def test_update_fascicolo(self, client, fascicolo, tipo_costruzione):
        """Test per l'aggiornamento di un Fascicolo."""
        url = reverse('fascicolo-detail', args=[fascicolo.id])
        updated_data = {
            "foglio": "30",
            "particella": "201",
            "tipo": tipo_costruzione.id,
            "indirizzo": "Vicolo Stretto, 3",
            "costruttore": "Impresa SRL",
            "note": "Fascicolo aggiornato"
        }
        response = client.patch(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        fascicolo.refresh_from_db()
        assert fascicolo.foglio == "30"
        assert fascicolo.note == "Fascicolo aggiornato"

    def test_delete_fascicolo(self, client, fascicolo):
        """Test per l'eliminazione di un Fascicolo."""
        url = reverse('fascicolo-detail', args=[fascicolo.id])
        response = client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Fascicolo.objects.count() == 0


# ----------------------
# Test Documento
# ----------------------

@pytest.mark.django_db
class TestDocumentoViewSet:

    def test_create_documento(self, client, documento_data):
        """Test per la creazione di un Documento."""
        url = reverse('documento-list')
        response = client.post(url, documento_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Documento.objects.count() == 1
        assert Documento.objects.first().numero == 1

    def test_list_documenti(self, client, documento):
        """Test per il recupero della lista di Documenti."""
        url = reverse('documento-list')
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['numero'] == documento.numero

    def test_retrieve_documento(self, client, documento):
        """Test per il dettaglio di un Documento."""
        url = reverse('documento-detail', args=[documento.id])
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['note'] == documento.note

    def test_update_documento(self, client, documento, tipo_documento):
        """Test aggiornamento di un Documento."""
        url = reverse('documento-detail', args=[documento.id])
        updated_data = {
            "tipo": tipo_documento.id,
            "numero": 5,
            "note": "Documento aggiornato"
        }
        response = client.patch(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        documento.refresh_from_db()
        assert documento.numero == 5
        assert documento.note == "Documento aggiornato"

    def test_delete_documento(self, client, documento):
        """Test eliminazione di un Documento."""
        url = reverse('documento-detail', args=[documento.id])
        response = client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Documento.objects.count() == 0


@pytest.mark.django_db
class TestSubalternoViewSet:

    def test_create_subalterno(self, client, subalterno_data):
        """Test per la creazione di un Subalterno."""
        url = reverse('subalterno-list')
        response = client.post(url, subalterno_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Subalterno.objects.count() == 1
        assert Subalterno.objects.first().sub == "SUB01"

    def test_list_subalterni(self, client, subalterno):
        """Test per il recupero della lista di Subalterni."""
        url = reverse('subalterno-list')
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['sub'] == subalterno.sub

    def test_retrieve_subalterno(self, client, subalterno):
        """Test per il dettaglio di un singolo Subalterno."""
        url = reverse('subalterno-detail', args=[subalterno.id])
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['sub'] == subalterno.sub

    def test_update_subalterno(self, client, subalterno, fascicolo):
        """Test per l'aggiornamento di un Subalterno."""
        url = reverse('subalterno-detail', args=[subalterno.id])
        updated_data = {
            "sub": "SUB02",
            "fascicolo": fascicolo.id
        }
        response = client.patch(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        subalterno.refresh_from_db()
        assert subalterno.sub == "SUB02"

    def test_delete_subalterno(self, client, subalterno):
        """Test per l'eliminazione di un Subalterno."""
        url = reverse('subalterno-detail', args=[subalterno.id])
        response = client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Subalterno.objects.count() == 0


@pytest.mark.django_db
class TestPraticaViewSet:

    def test_create_pratica(self, client, pratica_data):
        """Test per la creazione di una Pratica."""
        url = reverse('pratica-list')
        response = client.post(url, pratica_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Pratica.objects.count() == 1

    def test_list_pratiche(self, client, pratica):
        """Test per il recupero della lista di Pratiche."""
        url = reverse('pratica-list')
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['note'] == pratica.note

    def test_retrieve_pratica(self, client, pratica):
        """Test per il dettaglio di una singola Pratica."""
        url = reverse('pratica-detail', args=[pratica.id])
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['note'] == pratica.note

    def test_update_pratica(self, client, pratica):
        """Test per l'aggiornamento di una Pratica."""
        url = reverse('pratica-detail', args=[pratica.id])
        updated_data = {
            "note": "Pratica aggiornata",
        }
        response = client.patch(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        pratica.refresh_from_db()
        assert pratica.note == "Pratica aggiornata"

    def test_delete_pratica(self, client, pratica):
        """Test per l'eliminazione di una Pratica."""
        url = reverse('pratica-detail', args=[pratica.id])
        response = client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Pratica.objects.count() == 0


@pytest.mark.django_db
class TestTipoDocumentoViewSet:

    def test_create_tipo_documento(self, client, tipo_documento_data):
        """Test per la creazione di un TipoDocumento."""
        url = reverse('tipo-documento-list')
        response = client.post(url, tipo_documento_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert TipoDocumento.objects.count() == 1
        assert TipoDocumento.objects.first().nome == "Documento Generico"

    def test_list_tipi_documenti(self, client, tipo_documento):
        """Test per il recupero della lista di Tipi di Documenti."""
        url = reverse('tipo-documento-list')
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['nome'] == tipo_documento.nome

    def test_retrieve_tipo_documento(self, client, tipo_documento):
        """Test per il dettaglio di un singolo TipoDocumento."""
        url = reverse('tipo-documento-detail', args=[tipo_documento.id])
        response = client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['nome'] == tipo_documento.nome

    def test_update_tipo_documento(self, client, tipo_documento):
        """Test per l'aggiornamento di un TipoDocumento."""
        url = reverse('tipo-documento-detail', args=[tipo_documento.id])
        updated_data = {
            "codice": "DOC02",
            "nome": "Documento Modificato"
        }
        response = client.patch(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        tipo_documento.refresh_from_db()
        assert tipo_documento.nome == "Documento Modificato"

    def test_delete_tipo_documento(self, client, tipo_documento):
        """Test per l'eliminazione di un TipoDocumento."""
        url = reverse('tipo-documento-detail', args=[tipo_documento.id])
        response = client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert TipoDocumento.objects.count() == 0
