from django import forms
from .models import *

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    Price = forms.IntegerField(label="Цена")
    port = forms.ModelChoiceField(queryset=Ports.objects.all(), label="Порты", empty_label="Порты не выбраны")
    captain = forms.ModelChoiceField(queryset=Captains.objects.all(), label="Капитаны", empty_label="Капитаны не выбраны")
    traveler = forms.ModelChoiceField(queryset=Travelers.objects.all(), label="Путешественники", empty_label="Путешественники не выбраны")