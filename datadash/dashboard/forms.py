from django import forms


class UploadPlanilhaForm(forms.Form):
    arquivo = forms.FileField(
        label="Selecione um arquivo CSV ou XLSX",
        required=True,
        widget=forms.FileInput(attrs={'accept': '.csv,.xlsx'})
    )
