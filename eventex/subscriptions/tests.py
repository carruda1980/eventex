from django.test import TestCase


class SubscriptionsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """GET /inscricao/ must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Subscribe form must contain html tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 5)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="submit')
