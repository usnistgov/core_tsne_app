"""TSNE Admin Forms
"""
from django import forms


class UploadMapForm(forms.Form):
    """
    Form to upload a new Map.
    """
    file = forms.FileField(label='Select a file', required=True,
                           widget=forms.FileInput(attrs={'class': 'form-control'}))
