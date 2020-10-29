from django.test import TestCase


class SubscriptionsTest(TestCase):
    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        response = self.client.get('/inscricao/')
        self.assertEqual(200, response.status_code)