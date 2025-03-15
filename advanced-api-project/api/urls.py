from django.urls import path
from .views import BookListView

urlpatterns = [
    path("list/", view=BookListView.as_view, name="list_books")
]
 