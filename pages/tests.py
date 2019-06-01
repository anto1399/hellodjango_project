from django.test import TestCase, SimpleTestCase

# Test for Rxistence of HomePage

class SimpleTests(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)