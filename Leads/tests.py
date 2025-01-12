from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.
class HomePageTest(TestCase):
     def test_status_codes(self):
         #TODO some sort of test
         response = self.client.get(reverse("landing_page"))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, "Layout/landing_page.html")
        
