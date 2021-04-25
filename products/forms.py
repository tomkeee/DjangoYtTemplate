from django import forms

from .models import Product

# class ProductForms(forms.Form):
#     Title=forms.CharField()

class ProductModelForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Title',
            'content'
        ]
    
    def clean_Title(self):
        data= self.cleaned_data.get('Title')
        if len(data)<4:
            raise forms.ValidationError("This is not long enough!")
        return data
