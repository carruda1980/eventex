from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        obj = Subscription.objects.create(
            name='Carlos Arruda',
            cpf='05620921611',
            email='caugustogarruda@gmail.com ',
            phone='31-996840810',
        )
        self.resp = self.client.get('/inscricao/{}/'.format(obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
#
    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = ('Carlos Arruda', '05620921611',
                    'caugustogarruda@gmail.com', '31-996840810')

        with self.subTest(self):
            for expected in contents:
                self.assertContains(self.resp, expected)
