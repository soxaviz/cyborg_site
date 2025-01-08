from .models import Stream, UserClip
from django import forms

class ClipForm(forms.ModelForm):
    class Meta:
        model = UserClip
        fields = ['name', 'url', 'preview']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Clip name'
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL'
            }),
            'preview': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['name', 'game', 'preview', 'is_live']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'stream name'
            }),
            "game": forms.Select(attrs={
                'class': 'form-select'
            }),
            'preview': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_live': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }