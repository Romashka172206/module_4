
from django.forms import ModelForm
from django.db import models
from django.core.exceptions import ValidationError


class Author(models.Model):

    title = models.CharField(max_length=3)

    description = models.TextField(max_length=3)

    price=models.DecimalField(max_digits=4,decimal_places=3)

    auction=models.BooleanField()

    image=models.ImageField()

class AdvertisementForm(ModelForm):
    class Meta:
        model = Author
        # fields = ['title','description','price','auction','image']
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0]=='?':
            raise ValidationError("Назвние не должно начинаться с вопросительного знака")
        return title


