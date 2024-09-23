import unittest
import json
from api import app


class TestAPI(unittest.TestCase):
    """
    Test cases on the segment matching API for checking correctness, functionality
    """
    def setUp(self):
        """ Set up the test environment """
        self.app = app.test_client()  # open a flask API test client
        self.app.testing = True
        with open('./test_audiences.json', 'r') as f:
            self.test_data = json.load(f)
        with open('./config.json') as f:
            config = json.load(f)
            self.match_threshold = config['match_threshold']

    def test_valid_data(self):
        """ Valid input test """
        response = self.app.post('/match',
                                 data=json.dumps(self.test_data),
                                 content_type='application/json'
                                 )
        data = json.loads(response.data)
        self.assertGreaterEqual(data, self.match_threshold)  # should return 400 for empty input
        print(data)

    def test_empty_data(self):
        """ Empty input test"""
        response = self.app.post('/match',
                                 data=json.dumps({"input_segments": []}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)  # should return 400 for empty input
        data = json.loads(response.data)
        print(data)

    # TODO: more test cases for other scenarios, like large scale input ...
    # def test_large_scale_input(self):
    #     """ Large input test """


if __name__ == '__main__':
    unittest.main()