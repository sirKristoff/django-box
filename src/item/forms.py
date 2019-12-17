from django import forms

from .models import Item 

class ItemForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)



class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Item.objects.filter(name__iexact=name)  # don't bother capitalization with __iexact
        if instance is not None: # instance was pass through while editing item
            qs = qs.exclude(pk=instance.pk) # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This name has already been used. Please try again.")
        return name