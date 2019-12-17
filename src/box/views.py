from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from item.models import Item


def home_page(request):
    title = "Welcome to Box page"
    content = "List of items"
    qs = Item.objects.all()[:3]

    context        = {"request": request, "title": title, "content": content, "items": qs}
    template_name  = "home.html"
    template_obj   = get_template(template_name)
    rendered_item  = template_obj.render(context)
    return HttpResponse(rendered_item)