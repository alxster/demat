from django import forms
from .models import TipoCostruzione, Fascicolo, Subalterno, Pratica, TipoDocumento, Documento

class TipoCostruzioneForm(forms.ModelForm):
    class Meta:
        model = TipoCostruzione
        fields = ['codice', 'nome']
        widgets = {
            'codice': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FascicoloForm(forms.ModelForm):
    class Meta:
        model = Fascicolo
        fields = ['foglio', 'particella', 'tipo', 'indirizzo', 'costruttore', 'note']
        widgets = {
            'foglio': forms.TextInput(attrs={'class': 'form-control'}),
            'particella': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'indirizzo': forms.TextInput(attrs={'class': 'form-control'}),
            'costruttore': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SubalternoForm(forms.ModelForm):
    class Meta:
        model = Subalterno
        fields = ['fascicolo', 'sub', 'note']
        widgets = {
            'fascicolo': forms.Select(attrs={'class': 'form-select'}),
            'sub': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PraticaForm(forms.ModelForm):
    class Meta:
        model = Pratica
        fields = ['fascicolo', 'subalterno', 'note']
        widgets = {
            'fascicolo': forms.Select(attrs={'class': 'form-select'}),
            'subalterno': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['codice', 'nome']
        widgets = {
            'codice': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'tipo', 'file', 'numero', 'numero_progressivo', 'data', 
            'approvato', 'data_approvazione', 'numero_protocollo', 
            'numero_protocollo_generale', 'numero_protocollo_settore', 
            'note', 'trascrizione', 'richiedente', 'destinatario', 
            'pratiche', 'subalterni', 'fascicoli'
        ]
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_progressivo': forms.NumberInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'approvato': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'data_approvazione': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numero_protocollo': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_protocollo_generale': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_protocollo_settore': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'trascrizione': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'richiedente': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
            'pratiche': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'subalterni': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'fascicoli': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
