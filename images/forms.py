from email.mime import image
from urllib import response

import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


# https://mysite.com:8000/images/create/?title=django%20and%20the%20duke&url=https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_%28Gottlieb%29.jpg
class ImageCreateForm(forms.ModelForm):
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data["url"]
        name = slugify(image.title)
        extension = image_url.rsplit(".", 1)[1].lower()
        image_name = f"{name}.{extension}"
        # download image from given URL
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image

    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widgets = {
            "url": forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg", "png"]
        extension = url.rsplit(".", 1)[1].lower()
        print(extension)
        if extension not in valid_extensions:
            raise forms.ValidationError(
                "The given URL does not match valid image extensions"
            )
        return url
