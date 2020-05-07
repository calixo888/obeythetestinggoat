from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from lists import views

class HomePageTest(TestCase):

    def test_root_url_is_home_page(self):
        root_page = resolve("/")
        self.assertEqual(root_page.func, views.index)

    def test_home_page_has_correct_html(self):
        http_request = HttpRequest()
        response = views.index(http_request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))  
