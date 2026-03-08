# Book Store

**A simple Django application for managing a book store. Users can add books with their title, author, and rating, and view the list of available books. Books can also be deleted from the list.**

## EZ start

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies
4. Run `docker-compose up -d` to start the PostgreSQL database
5. Run `python manage.py migrate` to apply database migrations
6. Run `python manage.py runserver` to start the development server
7. Access the application at `http://localhost:8000`

## Endpoints

| Method | Endpoint            | Description            |
| ------ | ------------------- | ---------------------- |
| GET    | /                   | Homepage               |
| GET    | /books              | Show the add book form |
| POST   | /books              | Add a new book         |
| POST   | /books/<id>/delete/ | Delete a book          |
