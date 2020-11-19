from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digits(self):
        """CPF must only accept digits. """
        data = dict(
            name='Carlos Arruda', cpf='abcd5678901',
            email='caugustogarruda@gmail.com', phone='31996840810'
        )

        form = SubscriptionForm(data)
        form.is_valid()

        self.assertListEqual(['cpf'], list(form.errors))