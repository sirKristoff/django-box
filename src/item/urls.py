"""item URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    item_list_view,
    item_create_view,
    item_detail_view,
    item_update_view,
    item_delete_view,
)


app_name = 'item'

urlpatterns = [
    path('', item_list_view, name='list'),
    path('create/', item_create_view, name='create'),
    path('<int:item_id>/', item_detail_view, name='detail'),
    path('<int:item_id>/edit/', item_update_view, name='update'),
    path('<int:item_id>/delete/', item_delete_view, name='delete'),
]
