from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for books
books = []

# CRUD Operations

# Create (POST)
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "published_year": data["published_year"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Retrieve (GET)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Update (PUT)
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book.update(data)
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Delete (DELETE)
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == "_main_":
    app.run(debug=True)