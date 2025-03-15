from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, BookDeleteView, BookUpdateView

urlpatterns = [
    path("books/list/", view=BookListView.as_view(), name="list-books"),
    path("books/create/", view=BookCreateView.as_view(), name="create-books"),
    path("books/delete/", view=BookDeleteView.as_view(), name="delete-books"),
    path("books/update/", view=BookUpdateView.as_view(), name="update-books"),
    path("books/detail/", view=BookDetailView.as_view(), name="detail-books"),
]
 