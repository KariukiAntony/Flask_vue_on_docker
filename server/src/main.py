from flask import Blueprint, jsonify, request
from flask.views import MethodView
from src.database import Database

book_bp = Blueprint("book_bp", __name__)


class Book(MethodView):
    def __init__(self) -> None:
        super().__init__()
        self.model = Database()

    def get(self, id):
        try:
            data = self.model.get_a_book(int(id))
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"status": "failed", "message": str(e)})

    def put(self, id):
        data = request.get_json()
        try:
            data.update({"id": int(id)})
            self.model.update_book(data)
            return (
                jsonify({"status": "success", "message": "book updated successfully"}),
                202,
            )

        except Exception as e:
            return jsonify({"status": "failed", "message": str(e)}), 500

    def delete(self, id):
        try:
            self.model.delete_book(int(id))
            return (
                jsonify({"status": "success", "message": "Book deleted successfully"}),
                204,
            )
        except Exception as e:
            return jsonify({"status": "failed", "message": str(e)})


class Books(MethodView):
    def __init__(self) -> None:
        super().__init__()
        self.model = Database()

    def get(self):
        books = self.model.get_all_books()
        return jsonify({"status": "success", "books": books}), 200

    def post(self):
        data = request.get_json()
        try:
            self.model.add_new_book(data)
            return jsonify({"status": "success", "message": "Book added"}), 201
        except Exception as e:
            return jsonify({"status": "failed", "message": str(e)})


book_bp.add_url_rule("/api/books/<string:id>", view_func=Book.as_view("book"))
book_bp.add_url_rule("/api/books", view_func=Books.as_view("books"))
