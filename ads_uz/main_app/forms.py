from django import forms

from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug"
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "title",
            "content",
            "preview",
            "price",
            "contact_data",
            "category"
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "preview": forms.FileInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "contact_data": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"})
        }
