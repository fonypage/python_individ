from django.contrib import admin
from .models import Genre, Author, Book

# 1) Инлайн-редактор: отображаем книги прямо на странице автора
class BookInline(admin.TabularInline):
    model = Book
    extra = 0                         # не показывать пустые формы
    fields = ('title', 'publication_date')
    show_change_link = True           # ссылка на редактирование книги

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # 1.1 какие столбцы показываем в списке
    list_display   = ('last_name', 'first_name', 'birth_date', 'book_count')
    # 1.2 фильтрация по полю
    list_filter    = ('birth_date',)
    # 1.3 поиск по имени и фамилии
    search_fields  = ('first_name', 'last_name')
    # 1.4 навигация по датам рождения
    date_hierarchy = 'birth_date'
    # добавляем инлайн-редактирование связанных книг
    inlines        = [BookInline]
    # вычисляемое поле: количество книг у автора
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Кол-во книг'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display    = ('name',)
    search_fields   = ('name',)
    ordering        = ('name',)     # сортировка по названию
    list_per_page   = 20           # сколько строк на страницу

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display     = ('title', 'author', 'publication_date')
    list_filter      = ('publication_date', 'genres')
    search_fields    = ('title', 'author__last_name', 'summary')
    date_hierarchy   = 'publication_date'
    ordering         = ('-publication_date',)  # по убыванию даты
    list_editable    = ('author',)              # редактировать поле прямо в списке
    filter_horizontal = ('genres',)             # удобный селектор ManyToMany
    autocomplete_fields = ('author',)           # автодополнение для FK
