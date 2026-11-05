from django.core import mail
from django.test import TestCase
from django.urls import reverse


class ContactTests(TestCase):
    def test_page_loads(self):
        self.assertEqual(self.client.get(reverse("contact")).status_code, 200)

    def test_valid_form_sends_email(self):
        r = self.client.post(reverse("contact"), {
            "name": "Ana Pérez", "email": "ana@example.com",
            "message": "Hola, quisiera reservar una mesa."})
        self.assertRedirects(r, reverse("contact"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Ana Pérez", mail.outbox[0].body)

    def test_invalid_form_sends_nothing(self):
        r = self.client.post(reverse("contact"), {
            "name": "A", "email": "no-es-correo", "message": "corto"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)
