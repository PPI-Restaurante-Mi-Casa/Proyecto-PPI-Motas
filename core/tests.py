from django.test import TestCase, Client
from django.urls import reverse


class CoreTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_carga_correctamente(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<html")
