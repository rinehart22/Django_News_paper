from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):

	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_url(self):
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code, 200)

	def test_template(self):
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code, 200)
		self.assertTemplateUsed(res, 'home.html')


class SignupPageTests(TestCase):
	username = 'admin' 
	email = 'admin@gmail.com' 

	def test_signup_page(self):
		response = self.client.get('/users/signup/')
		self.assertEqual(response.status_code, 200)

	def test_url_sign(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)

	def test_template_sign(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response,'signup.html')

	def test_signup_form(self):
		new_user = get_user_model().objects.create_user(self.username, self.email)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		self.assertEqual(get_user_model().objects.all()[0].username, self.username)
		self.assertEqual(get_user_model().objects.all()[0].email, self.email)
