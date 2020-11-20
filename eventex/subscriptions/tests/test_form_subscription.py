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
        form = self.make_cpf_validate(cpf='abcd56789011')

        self.assertListEqual(['cpf'], list(form.errors))

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits. """
        form = self.make_cpf_validate(cpf='1234')

        self.assertListEqual(['cpf'], list(form.errors))

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_cpf_validate(name="CARLOS arruda")
        self.assertEqual('Carlos Arruda', form.cleaned_data['name'])

    def make_cpf_validate(self, **kwargs):
        valid = dict(
            name='Carlos Arruda', cpf='12345678901',
            email='caugustogarruda@gmail.com', phone='31996840810'
        )
        data = dict(valid,  **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
