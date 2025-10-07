from django.test import TestCase

from catalog.models import Author, Genre, Language, Book, BookInstance

# Create your tests here.

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods"""
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)

        field_label = author._meta.get_field('first_name').verbose_name

        self.assertIn(field_label, 'first name')
    
    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)

        max_length = author._meta.get_field('first_name').max_length

        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        author = Author.objects.get(id=1)

        field_label = author._meta.get_field('last_name').verbose_name

        self.assertIn(field_label, 'last name')
    
    def test_last_name_max_length(self):
            author = Author.objects.get(id=1)

            max_length = author._meta.get_field('last_name').max_length

            self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)

        expected_object_name = f'{author.last_name}, {author.first_name}'

        self.assertIn(str(author), expected_object_name)

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)

        field_label = author._meta.get_field('date_of_birth').verbose_name

        self.assertIn(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)

        field_label = author._meta.get_field('date_of_death').verbose_name

        self.assertIn(field_label, 'died')

    def test_get_absolute_url(self):
        """Test URL for Author instance."""
        author = Author.objects.get(id=1)
        
        self.assertIn(author.get_absolute_url(), '/catalog/author/1')


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(
            title='Sherlock Holmes',
            summary='test summary',
            isbn='9780679785467'
        )

    def test_title_label(self):
        book = Book.objects.get(id=1)

        field_label = book._meta.get_field('title').verbose_name

        self.assertIn(field_label, 'title')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)

        max_length = book._meta.get_field('title').max_length

        self.assertEqual(max_length, 200)

    def test_author_label(self):
         book = Book.objects.get(id=1)

         field_label = book._meta.get_field('author').verbose_name

         self.assertIn(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)

        field_label = book._meta.get_field('summary').verbose_name

        self.assertIn(field_label, 'summary')
    
    def test_summary_max_length(self):
         book = Book.objects.get(id=1)

         max_length = book._meta.get_field('summary').max_length

         self.assertEqual(max_length, 1000)

    def test_isbn_label(self):
         book = Book.objects.get(id=1)

         field_label = book._meta.get_field('isbn').verbose_name

         self.assertIn(field_label, 'ISBN')

    def test_isbn_max_length(self):
         book = Book.objects.get(id=1)

         max_length = book._meta.get_field('isbn').max_length

         self.assertEqual(max_length, 13)

    def test_genre_label(self):
        book = Book.objects.get(id=1)

        field_label = book._meta.get_field('genre').verbose_name

        self.assertIn(field_label, 'genre')

    def test_language_label(self):
        book = Book.objects.get(id=1)

        field_label = book._meta.get_field('language').verbose_name

        self.assertIn(field_label, 'language')

    def test_get_absolute_url(self):
        """Test URL for Book instance"""
        book = Book.objects.get(id=1)

        self.assertIn(book.get_absolute_url(), '/catalog/book/1')


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='Horror')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)

        field_label = genre._meta.get_field('name').verbose_name

        self.assertIn(field_label, 'name')

    def test_help_text(self):
        genre = Genre.objects.get(id=1)

        field_help_text = genre._meta.get_field('name').help_text

        self.assertIn(field_help_text, 'Enter a book genre (eg. Science Fiction)')

    # def test_get_absolute_url(self):
    #         genre = Genre.objects.get(id=1)
            # This will also fail if the URLConf is not defined.
    #         self.assertEqual(genre.get_absolute_url(), '/catalog/genre/1')


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Language.objects.create(name='Urdu')

    def test_name_label(self):
        language = Language.objects.get(id=1)

        field_label = language._meta.get_field('name').verbose_name

        self.assertIn(field_label, 'name')
    
    def test_help_text(self):
        language = Language.objects.get(id=1)

        field_help_text = language._meta.get_field('name').help_text

        self.assertIn(field_help_text, 'Enter the book\'s natural language (eg. English, French, Japanese etc.)')

    # def test_get_absolute_url(self):
    #     """Test URL for Language instance"""
    #     language = Language.objects.get(id=1)

    #     self.assertEqual(language.get_absolute_url(), '/catalog/language/1')


class ModelRelationshipTest(TestCase):

    def test_book_author_foreign_key(self):
        """Test foreign key relationship from book to author"""
        author = Author.objects.create(
            first_name='William',
            last_name='Shakespeare'
        )
        book = Book.objects.create(
            title='Macbeth',
            author=author
        )

        self.assertEqual(book.author, author)

        self.assertIn(book, author.book_set.all())

    def test_book_language_foreign_key(self):
        """Test foreign key relationship from book to language"""
        language = Language.objects.create(name='English')
        book = Book.objects.create(
            title='Hamlet',
            language=language
        )

        self.assertEqual(book.language, language)

        self.assertIn(book, language.book_set.all())

    def test_book_genre_many_to_many(self):
        """Test many to many relationship from book to genre"""
        genre1 = Genre.objects.create(name='Fantasy')
        genre2 = Genre.objects.create(name='Sci-Fi')

        book = Book.objects.create(title='The Lord of the Rings')
        book.genre.add(genre1, genre2)

        self.assertEqual(book.genre.count(), 2)
        self.assertIn(genre1, book.genre.all())
        self.assertIn(genre2, book.genre.all())

        self.assertIn(book, genre1.book_set.all())
        self.assertIn(book, genre2.book_set.all())

# TODO: create TestCase for book instances
class BookInstanceTestCase(TestCase):

    def test_id_label(self):
        book = Book.objects.create(title='Test Book')
        bookinst = BookInstance.objects.create(
            book=book,
            imprint='Test Imprint',
            due_back='2024-12-31',
            status='o'
        )

        field_label = bookinst._meta.get_field('id').verbose_name

        self.assertIn(field_label, 'id')

    def test_book_label(self):
        book = Book.objects.create(title='Test Book')
        bookinst = BookInstance.objects.create(
            book=book,
            imprint='Test Imprint',
            due_back='2025-10-11',
            status='o'
        )

        field_label = bookinst._meta.get_field('book').verbose_name

        self.assertIn(field_label, 'book')

    def test_imprint_label(self):
        book = Book.objects.create(title='Test Book')
        bookinst = BookInstance.objects.create(
            book=book,
            imprint='Test Imprint',
            due_back='2024-12-31',
            status='o'
        )

        field_label = bookinst._meta.get_field('imprint').verbose_name

        self.assertIn(field_label, 'imprint')

    def test_imprint_max_length(self):
        book = Book.objects.create(title='Test Book')
        bookinst = BookInstance.objects.create(
            book=book,
            imprint='Test Imprint',
            due_back='2024-12-31',
            status='o'
        )

        max_length = bookinst._meta.get_field('imprint').max_length

        self.assertEqual(max_length, 200)


