from django.db import models
from .apps import ItemConfig


class Item(models.Model):
    """
    Category of item describing its properties.
    """
    # id = models.IntegerField() # pk
    # how to setup foreign key - lesson 39
    name = models.CharField(null=False, blank=False, max_length=120)
    image = models.ImageField(upload_to='img/', blank=True, null=False, default='/static/item/img/default_item_image.png')
    description = models.TextField(null=False, blank=True)

    def __repr__(self):
        return f"<Item({self.id}): '{self.name}'>"

    def get_absolute_url(self):
        return f"/{ItemConfig.name}/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
