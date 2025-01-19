# from django.test import TestCase, Client
# from django.urls import reverse
# import json

# class GenerateMealPlanJSONTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('generate_meal_plan')  # Update this with your URL pattern name

#     def test_valid_json_input(self):
#         """Test if valid JSON data is parsed correctly."""
#         valid_data = {
#             "key": "value"  # Replace with your expected input
#         }
#         response = self.client.post(
#             self.url,
#             data=json.dumps(valid_data),
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json().get('status'), 'success')

#     def test_invalid_json_input(self):
#         """Test if invalid JSON data is handled gracefully."""
#         invalid_data = "{'key': 'value'}"  # Invalid JSON
#         response = self.client.post(
#             self.url,
#             data=invalid_data,
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, 500)
#         self.assertIn('error', response.json())
#         self.assertIn('Expecting property name', response.json()['error'])
