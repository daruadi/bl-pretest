import requests
import unittest

class TestGetPosts(unittest.TestCase):
	data = None

	def setUp(self):
		self.data = requests.get('https://jsonplaceholder.typicode.com/posts')

	def test_Userid_is_integer(self):
		found = 0
		for item in self.data.json():
			if isinstance(item['userId'], int) == False:
				found = found + 1
				break
		self.assertEqual(found, 0, 'Found item with userId is not integer')

	def test_Id_is_integer(self):
		found = 0
		for item in self.data.json():
			if isinstance(item['id'], int) == False:
				found = found + 1
				break
		self.assertEqual(found, 0, 'Found item with Id is not integer')

	def test_Title_is_string(self):
		found = 0
		for item in self.data.json():
			if isinstance(item['title'], str) == False:
				found = found + 1
				break
		self.assertEqual(found, 0, 'Found item with Title is not string')

	def test_Body_is_string(self):
		found = 0
		for item in self.data.json():
			if isinstance(item['body'], str) == False:
				found = found + 1
				break
		self.assertEqual(found, 0, 'Found item with Body is not string')

class TestPostPosts(unittest.TestCase):
	def test_get_response(self):
		body = {
			'title':'recomendation',
			'body':'motorcycle',
			'userId': 12
		}
		data = requests.post('https://jsonplaceholder.typicode.com/posts', data=body)
		response = data.json()
		self.assertEqual(response['id'], 101, 'response is not 101')

if __name__ == '__main__':
	unittest.main()
