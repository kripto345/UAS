from django import forms

class CaesarCipherForm(forms.Form):
    CHOICES = [('encrypt', 'Encrypt'), ('decrypt', 'Decrypt')]
    text = forms.CharField(widget=forms.Textarea, label='Text')
    shift = forms.IntegerField(label='Shift')
    mode = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Mode')
