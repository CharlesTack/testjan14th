from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content for testing"""
        self.about_content = About(
            title="About me",
            content="Sample about me content")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Tests if the about page is rendered with the collaborate form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About me", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)