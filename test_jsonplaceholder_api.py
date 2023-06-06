import unittest
import requests

class TestJsonPlaceholderAPI(unittest.TestCase):
    def test_get_posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

        # Check that each post has the necessary keys
        for post in data:
            self.assertIn("userId", post)
            self.assertIn("id", post)
            self.assertIn("title", post)
            self.assertIn("body", post)

    def test_get_comments(self):
        response = requests.get("https://jsonplaceholder.typicode.com/comments")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

        # Check that each comment has the necessary keys
        for comment in data:
            self.assertIn("postId", comment)
            self.assertIn("id", comment)
            self.assertIn("name", comment)
            self.assertIn("email", comment)
            self.assertIn("body", comment)

    def test_get_albums(self):
        response = requests.get("https://jsonplaceholder.typicode.com/albums")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

        # Check that each album has the necessary keys
        for album in data:
            self.assertIn("userId", album)
            self.assertIn("id", album)
            self.assertIn("title", album)

    def test_get_photos(self):
        response = requests.get("https://jsonplaceholder.typicode.com/photos")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

        # Check that each photo has the necessary keys
        for photo in data:
            self.assertIn("albumId", photo)
            self.assertIn("id", photo)
            self.assertIn("title", photo)
            self.assertIn("url", photo)
            self.assertIn("thumbnailUrl", photo)        

    def test_get_todos(self):
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

        # Check that each todos has the necessary keys
        for todos in data:
            self.assertIn("userId", todos)
            self.assertIn("id", todos)
            self.assertIn("title", todos)
            self.assertIn("completed", todos)

    def test_get_users(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        
        # Check that each user has the necessary keys
        for user in data:
            self.assertIn("id", user)
            self.assertIn("name", user)
            self.assertIn("username", user)
            self.assertIn("email", user)
            self.assertIn("address", user)
            self.assertIn("phone", user)
            self.assertIn("website", user)
            self.assertIn("company", user)

            # Check that the address has the necessary keys
            self.assertIn("street", user["address"])
            self.assertIn("suite", user["address"])
            self.assertIn("city", user["address"])
            self.assertIn("zipcode", user["address"])
            self.assertIn("geo", user["address"])

            # Check that the geo has the necessary keys
            self.assertIn("lat", user["address"]["geo"])
            self.assertIn("lng", user["address"]["geo"])

            # Check that the company has the necessary keys
            self.assertIn("name", user["company"])
            self.assertIn("catchPhrase", user["company"])
            self.assertIn("bs", user["company"])


if __name__ == "__main__":
    unittest.main()
