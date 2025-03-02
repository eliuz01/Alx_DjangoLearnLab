from django.contrib import admin
from .models import Book
from  django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields displayed in the admin interface for an existing user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields displayed when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active')
        }),
    )

    # Searchable fields in the user list
    search_fields = ('username', 'email')

    # Filters available in the admin list view
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # List of fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'is_staff')


# Register CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)


# Book Admin
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters to the admin interface for easy navigation
    list_filter = ('publication_year', 'author')

    # Enable search functionality on the specified fields
    search_fields = ('title', 'author')


# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)
