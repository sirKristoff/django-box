from django.db import models
from django.db.models import Q
from .apps import ItemConfig



class ItemQuerySet(models.QuerySet):
    """
    docstring for ItemQuerySet
    """

    def search(self, query):
        if query is None:
            return self.all()
        lookup = (Q(name__iexact=query) | Q(description__icontains=query))
        return self.filter(lookup)



class ItemManager(models.Manager):
    """
    docstring for ItemManager
    """

    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query)



class Item(models.Model):
    """
    Category of item describing its properties.
    """
    # id = models.IntegerField() # pk
    # how to setup foreign key - lesson 39
    name = models.CharField(unique=True, null=False, blank=False, max_length=120)
    image = models.ImageField(upload_to='img/', blank=True, null=False, default='/static/item/img/default_item_image.png')
    description = models.TextField(null=False, blank=True)

    objects = ItemManager()
    
    class Meta:
        ordering = ['id', '-name']
    
    def __repr__(self):
        return f"<Item({self.id}): '{self.name}'>"

    def get_absolute_url(self):
        return f"/{ItemConfig.name}/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
