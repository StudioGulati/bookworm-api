import base64
import unittest
import unittest.mock

from flask import Flask

import main


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_ocr(self):
        with self.app.app_context(), open('resources/wakeupcat.jpg', 'rb') as image_file:
            content = base64.b64encode(image_file.read())
            request = unittest.mock.Mock(data=content)
            response = main.ocr(request)
            assert response.status_code == 200
            assert response.get_json()
            print(response.get_json())


if __name__ == '__main__':
    unittest.main()
