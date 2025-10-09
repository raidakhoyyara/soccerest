from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category"]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg px-3 py-2 focus:border-amber-500 focus:ring focus:ring-amber-200 transition-colors',
                'placeholder': 'Contoh: Bola Adidas'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg px-3 py-2 focus:border-amber-500 focus:ring focus:ring-amber-200 transition-colors',
                'placeholder': 'Contoh: 250000'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg px-3 py-2 focus:border-amber-500 focus:ring focus:ring-amber-200 transition-colors',
                'rows': 4, 
                'placeholder': 'Jelaskan detail produk Anda di sini...'
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg px-3 py-2 focus:border-amber-500 focus:ring focus:ring-amber-200 transition-colors',
                'placeholder': 'https://example.com/gambar-produk.jpg'
            }),
            'category': forms.Select(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg px-3 py-2 focus:border-amber-500 focus:ring focus:ring-amber-200 transition-colors'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)