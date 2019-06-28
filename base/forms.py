
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from .models import Base
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


class FormBase(ModelForm):
    algoritmo = forms.CharField(widget=CKEditorWidget(config_name='edicion'))
    # usro = forms.ForeignKey(required=False)

    # def clean_usro(self):
    #     usro = self.cleaned_data['usro']
    #     return usro

    class Meta:
        model = Base
        # exclude = ('usro',)
        fields = ['tema','observacion','problema', 'clave', 'solucion', 'algoritmo', 'referencia', 'usro']
        labels = {
            'tema': _('Tema'),
            'observacion': _('Observaciones'),
            'problema': _('Problema'),
            'clave': _('Palabras Clave'),
            'solucion': _('Solución'),
            'algoritmo': _('Algoritmo'),
            'referencia': _('Referencia')
        }
        # help_texts = {
        #     'problema': _(Base.problema)
        # }
        error_messages={
            'problema': {
                'required': _('Ingrese un problema')
            },
            'tema':{
                'required': _('Ingrese un tema')
            },
            'solucion':{
                'required': _('Ingrese una solución')
            },
            'clave':{
                'required': _("Ingrese una o más palabras clave")
            }
        }

