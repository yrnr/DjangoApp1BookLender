from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Book 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
ydict = {
    'ykey1': 'You are viewing yapp.views.ydict1[ykey1]',
    'ykey2': 'You are viewing yapp.views.ydict1[ykey1]',
}

books = [
    {'booknumber': '1', 'title': 'Matilda', 'author':'Roald Dahl'},
    {'booknumber': '2', 'title': 'Persuation', 'author':'Jane Austen'},
    {'booknumber': '3', 'title': 'Animal Farm', 'author':'George Orwell'},
    {'booknumber': '4', 'title': 'Diary of a Winpy Kid', 'author':'Jeff Kinley'},
]
def home_httpresponse(request):
    return HttpResponse('<font color=#444444><h4>You are viewing:</h4> <h1>Django App <i>yapp</i> Home Page</h1> <h5>From: <i>yapp/views.py</i></h5></font>')

def about_httpresponse(request):
    return HttpResponse('<font color=#666677><h4>You are viewing:</h4> <h1>Django App <i>yapp</i> About Page</h1> <h5>From: <i>yapp/views.py</i></h5></font>')

def home_render(request):
    return render(request, 'yapp/home_render.html', ydict)

def about_render(request):
    return render(request, 'yapp/about_render.html')

def home(request):
    # ylibrary = { 'books': table_of_rows }
    # The keys of books dictionary will be given to home.html template for parsing
    # In this case, ylibrary has just one key, that is 'books'
    # 'books' is a table of 4 columns and 3 rows
    ylibrary = { 'books': Book.objects.all() }
    # All objects-of-model-Book / rows-of-database-table-Book is given to home.html template for parsing
    # In this case, ylibrary has just one key, that is 'books'
    return render(request, 'yapp/home.html', ylibrary)


def about(request):
    return render(request, 'yapp/about.html')


class BookListView(ListView):
    model = Book
    template_name = 'yapp/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-title']
    paginate_by = 4

class BookDetailView(DetailView):
    model = Book
    
class BookCreateView(LoginRequiredMixin, CreateView):
    # LoginRequiredMixin is the class-based-view counterpart 
    # of @login_required decorator of function-based-view
    model = Book
    fields = ['title', 'author']

    # Link this new book with a donor, in our case, the user 
    # who is logged in and doing the create/add book (donor of new book to the library)
    def form_valid(self, form) -> HttpResponse:
        form.instance.donor = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # LoginRequiredMixin is the class-based-view counterpart 
    # of @login_required decorator of function-based-view
    model = Book
    fields = ['title', 'author']

    # Link this new book with a donor, in our case, the user 
    # who is logged in and doing the create/add book (donor of new book to the library)
    def form_valid(self, form) -> HttpResponse:
        form.instance.donor = self.request.user
        return super().form_valid(form)

    def test_func(self): 
        # This is a UserPassesTestMixin's function
        # We are overriding this function here
        # To ensure, update-book-detail can be done by its donor only
        book = self.get_object()
        if self.request.user == book.donor:
            return True
        else:
            return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'
    def test_func(self): 
        # This is a UserPassesTestMixin's function
        # We are overriding this function here
        # To ensure, delete-book can be done by its donor only
        book = self.get_object()
        if self.request.user == book.donor:
            return True
        else:
            return False
        
class AuthorBookListView(ListView):
    model = Book
    template_name = 'yapp/author_bookslist.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-title']
    paginate_by = 3

    def get_queryset(self):
        print(f'self.kwargs={self.kwargs.items()} Model={self.model}')
        self.author = self.kwargs["author"]
        return Book.objects.filter(author=self.author)
