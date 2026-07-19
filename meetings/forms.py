from django import forms
from .models import Meeting


class MeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting

        fields = ['title', 'audio']

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Meeting Title'
            }),

            'audio': forms.FileInput(attrs={
                'class': 'form-control'
            }),

        }