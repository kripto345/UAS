from django.shortcuts import render
from .forms import CaesarCipherForm

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def cipher_view(request):
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            shift = form.cleaned_data['shift']
            mode = form.cleaned_data['mode']
            result = caesar_cipher(text, shift, mode)
            return render(request, 'cipher/result.html', {'form': form, 'result': result})
    else:
        form = CaesarCipherForm()
    return render(request, 'cipher/index.html', {'form': form})


# Create your views here.
