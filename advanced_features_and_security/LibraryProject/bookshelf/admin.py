from django.contrib import admin
from .models import Book
from  django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    pass
admin.site.register(CustomUser, CustomUserAdmin)



# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    #Add filters to the admin interface for easy navigation
    list_filter = ('publication_year', 'author')

    #Enable search functionality on the specified fields
    search_fields = ('title', 'author')

#Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)