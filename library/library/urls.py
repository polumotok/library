"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app_books.views import BooksViewSet
from app_readers.views import ReadersView, LocationBookView

router_books = routers.DefaultRouter()
router_books.register(r"books", BooksViewSet, basename="books")
router_readers = routers.DefaultRouter()
router_readers.register(r"readers", ReadersView, basename="readers")
router_LocationBook = routers.DefaultRouter()
router_LocationBook.register(r"LocationBook", LocationBookView, basename="LocationBook")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router_books.urls)),
    path("api/", include(router_readers.urls)),
    path("api/", include(router_LocationBook.urls)),
]
