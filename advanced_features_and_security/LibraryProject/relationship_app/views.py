""" 
A view in django is a a function or a class that 
 -accepts a http reques
 -retuns a http response
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import Author
from .models import UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required



# Function-based view to list all books
def list_books(request):
    books = Book.objects.all() # Query all books from the database

    #Render the 'list_books.html' template and pass the books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (CBV) to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # This CBV will work with the Library model
    template_name = 'relationship_app/library_detail.html'  # Template to render the library details
    context_object_name = 'library'  # The context variable for the template
    
#View for Login
# View for Login
def user_login(request):
    # If the method is POST, we handle the login attempt
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Initialize the authentication form with POST data
        if form.is_valid():  # If the form is valid, we authenticate the user
            username = form.cleaned_data.get('username')  # Get cleaned data from form
            password = form.cleaned_data.get('password')  # Get password
            user = authenticate(request, username=username, password=password)  # Authenticate the user
            if user is not None:  # If authentication is successful
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to home (or another page)
    else:
        form = AuthenticationForm()  # If GET request, create an empty form

    # Render the login template with the form passed in context
    return render(request, 'relationship_app/login.html', {'form': form})

# View for Logout
def user_logout(request):
    logout(request)  # Logs the user out
    return render(request, 'relationship_app/logout.html')  # Render the logout template

# View for Registration
def register(request):
    # If the method is POST, handle the registration form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Create a user creation form with POST data
        if form.is_valid():  # If the form is valid, save the new user
            form.save()  # Save the new user to the database
            return redirect('login')  # After successful registration, redirect to login page
    else:
        form = UserCreationForm()  # If GET request, create an empty form

    # Render the registration template with the form passed in context
    return render(request, 'relationship_app/register.html', {'form': form})

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == UserProfile.Member

# View for Admins
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# View for Members
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# View to add a book (Create)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = get_object_or_404(Author, id=author_id)
        
        # Create and save the new book
        book = Book.objects.create(title=title, author=author)
        return redirect('list_books')  # Redirect to the book list view

    return render(request, 'relationship_app/add_book.html')

# View to edit a book (Update)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, id=author_id)
        book.save()  # Save the updated book
        
        return redirect('list_books')  # Redirect to the book list view
    
    return render(request, 'relationship_app/edit_book.html', {'book': book})


# View to delete a book (Delete)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        return redirect('list_books')  # Redirect to the book list view
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})