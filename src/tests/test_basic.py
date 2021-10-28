import unittest
import requests

class TestRestCall(unittest.TestCase):

	def test_rest_call(self):
		r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
		client_data = r.json()

		print(client_data)
		self.assertTrue(client_data['userId'] == 1)



if __name__ == '__main__':
    unittest.main()
