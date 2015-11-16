from django import forms
from django.forms import MultipleChoiceField, ChoiceField
from peteslist.models import Post, Category, Image, Type

CONTACT_CHOICES = (
    ('by_phone', 'By Phone'),
    ('by_text', 'By Text')
    )


class ForSaleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('type', 'category', 'by_phone', 'by_text', 'phone_number',
                  'contact_name', 'title', 'price', 'specific_location',
                  'description', 'condition')

        widgets = {
            # 'type': forms.TextInput(attrs={'class': 'required'}),
            # 'category': forms.ModelChoiceField(Category.objects.filter(type=type))
            # 'title': forms.TextInput(attrs={'class': 'required'}),
            # 'description': forms.TextInput(attrs={'class': 'required'}),
            # 'by_phone': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'by_text': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'phone_number': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'contact_name': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'price': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'specific_location': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'manufacturer': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'model_name': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'serial_num': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'dimensions': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'condition': forms.CheckboxInput(attrs={'class': 'optional'})
            # # 'by_phone': forms.BooleanField(attrs={'class': 'form_control'})
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=120)


class KeywordForm(forms.Form):
    keywords = forms.CharField(label='Add Keyword(s)', max_length=50)
