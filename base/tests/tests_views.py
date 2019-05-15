from django.test import TestCase
from django.urls import reverse



class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))  # comprueba "name" del URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Bitácora')
    def test_about_us_page_works(self):
        response = self.client.get(reverse("acerca"))  # comprueba "name" del URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'acerca.html')
        self.assertContains(response, 'Bitácora')