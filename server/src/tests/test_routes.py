import json
from . import TestBaseCase


class TestRoutes(TestBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = self.app.test_client()
        self.id = 1

    def test_index(self) -> None:
        resp = self.client.get(f"/books/{self.id}")

        self.assertDictEqual(
            resp.get_json(), {"message": f"Hello this is the id: {self.id}"}
        )
        self.assertEqual(resp.status_code, 200)

    def test_book_create(self) -> None:
        book = {"title": "The river between", "author": "Margaret Ogola", "read": True}
        resp = self.client.post(
            "/books",
            data=json.dumps(book),
            headers={"Content-Type": "application/json"},
        )
        self.assertFalse(resp.status_code != 201)
        self.assertEqual(
            resp.get_json(),
            {
                "message": "Book added",
                "status": "success",
            },
        )

    def test_get_books(self) -> None:
        resp = self.client.get("/books")
        keys = resp.get_json().keys()
        self.assertEqual(resp.status_code, 200)
        self.assertIn("books", keys)

    def test_book_update(self):
        data = {"title": "updated title", "author": "elon margaret", "read": False}
        resp = self.client.put(
            f"/books/{self.id}",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(resp.status_code, 202)

    def test_delete_book(self) -> None:
        resp = self.client.delete(f"/books/{self.id}")
        self.assertEqual(resp.status_code, 204)
        self.assertIs(resp.data.decode("utf-8"), "")
