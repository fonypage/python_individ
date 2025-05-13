from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField("Название жанра", max_length=100, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name  = models.CharField("Фамилия", max_length=100)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Book(models.Model):
    title            = models.CharField("Название книги", max_length=200)
    author           = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genres           = models.ManyToManyField(Genre, verbose_name="Жанры")
    publication_date = models.DateField("Дата публикации")
    summary          = models.TextField("Аннотация", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book_detail', args=[self.id])