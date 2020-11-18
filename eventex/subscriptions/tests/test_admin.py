from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def test_has_action(self):
        """Action mark_as_paid should be installed."""
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid"""
        Subscription.objects.create(
            name='Carlos Arruda', cpf='12345678911',
            email='caugustogarruda@gmail.com', phone='31996840810'
        )
        queryset = Subscription.objects.all()

        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        model_admin.mark_as_paid(None, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True))