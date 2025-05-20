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
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        lat = cleaned_data.get("latitude")
        lon = cleaned_data.get("longitude")

        if lat is None or lon is None:
            raise forms.ValidationError("Lokasi tidak terdeteksi. Aktifkan lokasi di browser.")