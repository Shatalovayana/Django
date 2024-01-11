from django import forms

from catalog.models import Product, Version

STOP_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price', 'image', 'is_published')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in STOP_WORDS:
            raise forms.ValidationError('Содержится недопустимое слово')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data in STOP_WORDS:
            raise forms.ValidationError('Содержится недопустимое слово')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
