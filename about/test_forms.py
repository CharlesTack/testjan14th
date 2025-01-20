from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Bob',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_in_form_is_invalid(self):
        """ Test for missing name"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), 
                         msg="Name was not provided, but the form is valid")

    def test_email_in_form_is_invalid(self):
        """ Test for missing email"""
        form = CollaborateForm({
            'name': 'Bob',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), 
                         msg="Email was not provided, but the form is valid")

    def test_message_in_form_is_invalid(self):
        """ Test for missing message"""
        form = CollaborateForm({
            'name': 'Bob',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), 
                         msg="Message was not provided, but the form is valid")