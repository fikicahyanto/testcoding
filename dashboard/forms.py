from django import forms
from dashboard.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'latitude', 'longitude']
        labels = {
            'message': 'Whats Happening?',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 2,'class':'form-control'}),
            'latitude': forms.HiddenInput(attrs={'id': 'id_latitude'}),
            'longitude': forms.HiddenInput(attrs={'id': 'id_longitude'}),
        }