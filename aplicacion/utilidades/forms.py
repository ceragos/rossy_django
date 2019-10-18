from django import forms


class FiltroRangoFechaForm(forms.Form):
    fecha_inicial = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'dd/mm/aaaa',
                                                                  'autocomplete': 'off'}))
    fecha_final = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                                'placeholder': 'dd/mm/aaaa',
                                                                'autocomplete': 'off'}))
