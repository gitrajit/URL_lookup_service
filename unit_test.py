import unittest
import urlapi
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test(self):
        response = requests.get('http://localhost:51/urlinfo/1/')
        self.assertEqual(response.json(), {"IP and port": ["1.1.1.0:80","1.1.1.1:81","test.domain:80"],
                                                "String": ["xxx","!&*","abc"]})
    def test2(self):
        response = requests.get('http://localhost:51/urlinfo/1/1.1.1.0:80/annnnnx')
        self.assertEqual(response.json(), {
                        "IP and port Safety": "BLOCKED!, hostname and port are listed in the database.",
                        "string safety": "String Safe as its not listed in database.",
                        "url": "http://1.1.1.0:80/annnnnx" })

    def test3(self):
        response = requests.get('http://localhost:51/urlinfo/1/test.domain:90/annnnnxxx')
        self.assertEqual(response.json(), {
                         "IP and port Safety": "hostname and port are Safe!",
                        "string safety": "BLOCKED, string listed in the database.",
                        "url": "http://test.domain:90/annnnnxxx" })

    def test4(self):
        response = requests.get('http://localhost:51/urlinfo/1/test.domain1:80/annnnnx')
        self.assertEqual(response.json(), {
                        "IP and port Safety": "hostname and port are Safe!",
                        "string safety": "String Safe as its not listed in database.",
                        "url": "http://test.domain1:80/annnnnx" })


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = urlapi.app.test_client()



if __name__ == "__main__":
    unittest.main()