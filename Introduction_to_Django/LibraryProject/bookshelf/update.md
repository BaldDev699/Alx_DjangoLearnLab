# Update Operation - Book Model

## Command
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.id,book.title, book.author, book.publication_year)

## Expected Output
1 Nineteen Eighty-Four George Orwell 1949