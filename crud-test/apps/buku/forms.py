from .models import buku
from django import forms

class bukuForm(forms.ModelForm):
    class Meta:
        model = buku
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(bukuForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Title"
        self.fields['description'].label = "Description"
