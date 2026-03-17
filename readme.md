# Book Store

**A simple Django application for managing a book store. Users can add books with their title, author, and rating, and view the list of available books. Books can also be deleted from the list.**

## EZ start

1. Clone the repository
2. Navigate to the project directory
3. run `docker compose up --build`
4. Open your browser and go to `http://localhost:3000` to see the application in action.

## Endpoints

| Method | Endpoint            | Description            |
| ------ | ------------------- | ---------------------- |
| GET    | /                   | Homepage               |
| GET    | /books              | Show the add book form |
| POST   | /books              | Add a new book         |
| POST   | /books/<id>/delete/ | Delete a book          |
