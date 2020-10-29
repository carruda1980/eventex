from django.test import TestCase


class SubscriptionsTest(TestCase):
    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        response = self.client.get('/inscricao/')
        self.assertEqual(200, response.status_code)

    def test_template(self):
        """GET /inscricao/ must use subscriptions/subscription_form.html"""
        response = self.client.get('/inscricao/')
        self.assertTemplateUsed(response, 'subscriptions/subscription_form.html')