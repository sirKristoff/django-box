from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from searches.models import SearchQuery
from .models import Item
from .forms import ItemModelForm



def item_list_view(request):
    # list out objects (could be search)
    query          = request.GET.get('q', None)
    qs             = Item.objects.search(query=query)
    template_name  = "item/list.html"
    context        = {'object_list': qs, 'query': query}
    SearchQuery.add_query(request)
    return render(request, template_name, context)


@staff_member_required
def item_create_view(request):
    form = ItemModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # form.save()
        obj = form.save(commit=False)
        # manipulate on object before commiting
        # obj.name = form.cleaned_data.get("name") + "!"
        obj.save()
        form = ItemModelForm()
        return redirect(obj.get_absolute_url())
    template_name  = "item/create.html"
    context        = {'form': form, 'title': "New Item:"}
    return render(request, template_name, context)


@login_required
def item_detail_view(request, item_id):
    # 1 object
    # retrieve/detail view
    obj            = get_object_or_404(Item, id=item_id)
    template_name  = "item/detail.html"
    context        = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def item_update_view(request, item_id):
    obj = get_object_or_404(Item, id=item_id)
    form = ItemModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(obj.get_absolute_url())
    template_name  = "item/update.html"
    context        = {"object": obj, 'form': form, 'title': f"Update {obj.name}"}
    return render(request, template_name, context)


@staff_member_required
def item_delete_view(request, item_id):
    obj            = get_object_or_404(Item, id=item_id)
    if request.method == "POST": # delete object only if posting
        obj.delete()
        return redirect("item:list")
    template_name  = "item/delete.html"
    context        = {"object": obj, 'form': None}
    return render(request, template_name, context)
