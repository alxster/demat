from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Fascicolo, Documento, TipoCostruzione, TipoDocumento, Pratica, Subalterno
from .serializers import (
    FascicoloSerializer,
    DocumentoSerializer,
    TipoCostruzioneSerializer,
    TipoDocumentoSerializer,
    PraticaSerializer,
    SubalternoSerializer,
)
from .forms import (
    TipoCostruzioneForm,
    FascicoloForm,
    SubalternoForm,
    PraticaForm,
    TipoDocumentoForm,
    DocumentoForm,
)


# API ViewSets
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

# Template-based views
# TipoCostruzione views
class TipoCostruzioneListView(ListView):
    model = TipoCostruzione
    template_name = 'catasto/tipocostruzione_list.html'
    context_object_name = 'tipi_costruzione'

class TipoCostruzioneDetailView(DetailView):
    model = TipoCostruzione
    template_name = 'catasto/tipocostruzione_detail.html'

class TipoCostruzioneCreateView(CreateView):
    model = TipoCostruzione
    form_class = TipoCostruzioneForm
    template_name = 'catasto/tipocostruzione_form.html'
    success_url = reverse_lazy('catasto:tipocostruzione-list')

class TipoCostruzioneUpdateView(UpdateView):
    model = TipoCostruzione
    form_class = TipoCostruzioneForm
    template_name = 'catasto/tipocostruzione_form.html'
    success_url = reverse_lazy('catasto:tipocostruzione-list')

class TipoCostruzioneDeleteView(DeleteView):
    model = TipoCostruzione
    template_name = 'catasto/tipocostruzione_confirm_delete.html'
    success_url = reverse_lazy('catasto:tipocostruzione-list')

# Fascicolo views
class FascicoloListView(ListView):
    model = Fascicolo
    template_name = 'catasto/fascicolo_list.html'
    context_object_name = 'fascicoli'

class FascicoloDetailView(DetailView):
    model = Fascicolo
    template_name = 'catasto/fascicolo_detail.html'

class FascicoloCreateView(CreateView):
    model = Fascicolo
    form_class = FascicoloForm
    template_name = 'catasto/fascicolo_form.html'
    success_url = reverse_lazy('catasto:fascicolo-list')

class FascicoloUpdateView(UpdateView):
    model = Fascicolo
    form_class = FascicoloForm
    template_name = 'catasto/fascicolo_form.html'
    success_url = reverse_lazy('catasto:fascicolo-list')

class FascicoloDeleteView(DeleteView):
    model = Fascicolo
    template_name = 'catasto/fascicolo_confirm_delete.html'
    success_url = reverse_lazy('catasto:fascicolo-list')

# Subalterno views
class SubalternoListView(ListView):
    model = Subalterno
    template_name = 'catasto/subalterno_list.html'
    context_object_name = 'subalterni'

class SubalternoDetailView(DetailView):
    model = Subalterno
    template_name = 'catasto/subalterno_detail.html'

class SubalternoCreateView(CreateView):
    model = Subalterno
    form_class = SubalternoForm
    template_name = 'catasto/subalterno_form.html'
    success_url = reverse_lazy('catasto:subalterno-list')

class SubalternoUpdateView(UpdateView):
    model = Subalterno
    form_class = SubalternoForm
    template_name = 'catasto/subalterno_form.html'
    success_url = reverse_lazy('catasto:subalterno-list')

class SubalternoDeleteView(DeleteView):
    model = Subalterno
    template_name = 'catasto/subalterno_confirm_delete.html'
    success_url = reverse_lazy('catasto:subalterno-list')

# Pratica views
class PraticaListView(ListView):
    model = Pratica
    template_name = 'catasto/pratica_list.html'
    context_object_name = 'pratiche'

class PraticaDetailView(DetailView):
    model = Pratica
    template_name = 'catasto/pratica_detail.html'

class PraticaCreateView(CreateView):
    model = Pratica
    form_class = PraticaForm
    template_name = 'catasto/pratica_form.html'
    success_url = reverse_lazy('catasto:pratica-list')

class PraticaUpdateView(UpdateView):
    model = Pratica
    form_class = PraticaForm
    template_name = 'catasto/pratica_form.html'
    success_url = reverse_lazy('catasto:pratica-list')

class PraticaDeleteView(DeleteView):
    model = Pratica
    template_name = 'catasto/pratica_confirm_delete.html'
    success_url = reverse_lazy('catasto:pratica-list')

# TipoDocumento views
class TipoDocumentoListView(ListView):
    model = TipoDocumento
    template_name = 'catasto/tipodocumento_list.html'
    context_object_name = 'tipi_documento'

class TipoDocumentoDetailView(DetailView):
    model = TipoDocumento
    template_name = 'catasto/tipodocumento_detail.html'

class TipoDocumentoCreateView(CreateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'catasto/tipodocumento_form.html'
    success_url = reverse_lazy('catasto:tipodocumento-list')

class TipoDocumentoUpdateView(UpdateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'catasto/tipodocumento_form.html'
    success_url = reverse_lazy('catasto:tipodocumento-list')

class TipoDocumentoDeleteView(DeleteView):
    model = TipoDocumento
    template_name = 'catasto/tipodocumento_confirm_delete.html'
    success_url = reverse_lazy('catasto:tipodocumento-list')

# Documento views
class DocumentoListView(ListView):
    model = Documento
    template_name = 'catasto/documento_list.html'
    context_object_name = 'documenti'

class DocumentoDetailView(DetailView):
    model = Documento
    template_name = 'catasto/documento_detail.html'

class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'catasto/documento_form.html'
    success_url = reverse_lazy('catasto:documento-list')

class DocumentoUpdateView(UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'catasto/documento_form.html'
    success_url = reverse_lazy('catasto:documento-list')

class DocumentoDeleteView(DeleteView):
    model = Documento
    template_name = 'catasto/documento_confirm_delete.html'
    success_url = reverse_lazy('catasto:documento-list')

# Index view
class IndexView(TemplateView):
    template_name = 'catasto/index.html'
