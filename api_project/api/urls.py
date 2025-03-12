from django.urls import path, include
from .views import BookList, BookViewSet, MyApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)), # This includes all routes registered with the router
    path('myapi/', MyApiView.as_view(), name='my-api'),
    path('api/token/', obtain_auth_token(), name='api-token'),
]