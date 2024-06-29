import json

import pytest
from . import TestBaseCase


class TestRoutes(TestBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = self.app.test_client()
        self.id = 1
        self.base_url = "/api"

    def test_index(self) -> None:
        print("Test index")
        resp = self.client.get(f"{self.base_url}/{self.id}")

        self.assertDictEqual(
            resp.get_json(), {"message": f"Hello this is the id: {self.id}"}
        )
        self.assertEqual(resp.status_code, 200)

    def test_create_book(self) -> None:
        book = {"title": "The river between", "author": "Margaret Ogola", "read": False}
        resp = self.client.post(
            f"{self.base_url}/books",
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
        
    def test_get_book(self):
        resp = self.client.get(f"{self.base_url}/books/{self.id}")
        data = resp.get_json()
        print(resp.data)
        self.assertTrue((resp.status_code == 200))
        # self.assertIn("id", data.keys())
        # self.assertEqual(data.get("id"), self.id)
        
    def test_get_books(self) -> None:
        resp = self.client.get(f"{self.base_url}/books")
        keys = resp.get_json().keys()
        self.assertEqual(resp.status_code, 200)
        self.assertIn("books", keys)

    def test_update_book(self):
        data = {"title": "updated title", "author": "updated author", "read": False}
        resp = self.client.put(
            f"{self.base_url}/books/{self.id}",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(resp.status_code, 202)

    def test_Delete_book(self) -> None:
        resp = self.client.delete(f"{self.base_url}/books/{self.id}")
        self.assertEqual(resp.status_code, 204)
        self.assertIs(resp.data.decode("utf-8"), "")
    
    def tearDown(self) -> None:
        super().tearDown()
        self.client = None