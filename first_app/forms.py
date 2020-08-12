from django import forms
from .models import SampleAttachment, Contact

class SmapleAttachmentForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    class Meta:
        model = SampleAttachment
        fields = ('email',)

