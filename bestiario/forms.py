from datetime import date

from django import forms

from .models import Avistamiento, Criatura


class AvistamientoForm(forms.ModelForm):
    class Meta:
        model = Avistamiento
        fields = ['criatura', 'nombre', 'email', 'fecha',
                  'cantidad', 'lugar', 'comentario']
        labels = {
            'criatura': 'Criatura que viste',
            'nombre': 'Tu nombre',
            'email': 'Tu correo',
            'fecha': 'Fecha del avistamiento',
            'cantidad': 'Cuantas viste',
            'lugar': 'Lugar',
            'comentario': 'Comentario (opcional)',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'comentario': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['criatura'].queryset = Criatura.objects.filter(visible=True)
        self.fields['criatura'].empty_label = "Elige una criatura"

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha > date.today():
            raise forms.ValidationError("La fecha no puede estar en el futuro.")
        return fecha

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 1:
            raise forms.ValidationError("Debes haber visto al menos una.")
        return cantidad