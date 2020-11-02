from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

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
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="submit')

    def test_csrf(self):
        """Html must contain csrf_token"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        self.data = dict(name="Carlos Arruda", cpf="12345678901", email="caugustogarruda@gmail.com", phone="31-996840810")
        self.resp = self.client.post('/inscricao/', self.data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        """Should send email to visitor"""
        self.assertEqual(1, len(mail.outbox))

    def test_subscribe_email_subject(self):
        """Subject should be 'Confirmação de inscrição'"""
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscribe_email_sender(self):
        """Sender should be 'contato@eventex.com.br'"""
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscribe_email_to(self):
        expect = ['contato@eventex.com.br', 'caugustogarruda@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscribe_email_body(self):
        self.assertIn('Carlos Arruda', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('caugustogarruda@gmail.com', self.email.body)
        self.assertIn('31-99684-0810', self.email.body)
