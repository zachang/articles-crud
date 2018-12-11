from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from rest_framework.reverse import reverse

from .models import Category, Article
from . import views

class CategoryModelTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""

        self.category_1 = Category.objects.create(category_name="Religion")
        self.category_2 = Category.objects.create(category_name="Music")

    def test_category_creation_is_successful(self):
        """Test the category model can create a category."""
        category_value = Category.objects.get(pk=1)
        category_count= Category.objects.count()

        self.assertEqual(category_value.category_name, self.category_1.category_name)
        self.assertEqual(category_value.id, self.category_1.id)
        self.assertEqual(category_count, 2)


class CategoryViewTestCase(TestCase):
    """Test suite for the api views."""


    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(first_name='Jacob', last_name='Nouwatin', 
            password='password', email='jacob@gmail.com', username="nerd"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.category_data = {'category_name': 'Politics'}
        self.category_data_2 = {'category_name': 'Dance'}
        self.response = self.client.post(reverse('blog:category-list'), self.category_data, format='json')
        self.response_2 = self.client.post(reverse('blog:category-list'), self.category_data_2, format='json')


    def test_api_can_create_a_category(self):
        """Test that the api can create category"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data['category_name'], self.category_data['category_name'])


    def test_api_can_create_a_category_no_auth_fails(self):
        """Test that the api can not create category without user authorization"""

        new_client = APIClient()
        new_category_data = {'category_name': 'War'}
        response = new_client.post(reverse('blog:category-list'), new_category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_update_a_category(self):
        """Test that the api can update category"""

        self.update_category_data = {'category_name': 'Music'}
        self.response_update = self.client.put(reverse('blog:category-detail',
             args=(self.response.data["id"],)), 
            self.update_category_data, format='json'
        )
        
        self.assertEqual(self.response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response_update.data['category_name'], 
            self.update_category_data['category_name']
        )


    def test_api_get_all_category(self):
        """Test that the api can retrieve category"""

        self.response_all = self.client.get(reverse('blog:category-list'), format='json')

        self.assertEqual(self.response_all.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response_all.data[0]['id'], self.response.data['id'])


    def test_api_can_get_single_category(self):
        """Test that the api can retrieve a category"""

        self.response_delete = self.client.delete(reverse('blog:category-detail',
            args=(self.response.data["id"],)), format='json')

        self.assertEqual(self.response_delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_single_category(self):
        """Test that the api can retrieve a category"""

        self.response_one = self.client.get(reverse('blog:category-detail',
            args=(self.response.data["id"],)), format='json')

        self.assertEqual(self.response_one.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response_one.data['category_name'], self.category_data['category_name'])