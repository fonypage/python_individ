from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
