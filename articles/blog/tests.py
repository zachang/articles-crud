from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

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

        self.client = APIClient()
        self.category_data = {'category_name': 'Politics'}
        self.response = self.client.post('/blog/api/category/', self.category_data, format='json')

    def test_api_can_create_a_category(self):
        """Test that the api can create category"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data['category_name'], self.category_data['category_name'])

    def test_api_can_update_a_category(self):
        """Test that the api can update category"""

        self.update_category_data = {'category_name': 'Music'}
        self.response_update = self.client.put(f'/blog/api/category/{self.response.data["id"]}/', 
            self.update_category_data, format='json'
        )
        
        self.assertEqual(self.response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response_update.data['category_name'], 
            self.update_category_data['category_name']
        )

    def test_api_get_all_category(self):
        """Test that the api can retrieve category"""

        self.response_all = self.client.get('/blog/api/category/', format='json')

        self.assertEqual(self.response_all.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response_all.data[0]['id'], self.response.data['id'])

    def test_api_can_get_single_category(self):
        """Test that the api can retrieve a category"""

        self.response_one = self.client.get(f'/blog/api/category/{self.response.data["id"]}/', format='json')

        self.assertEqual(self.response_one.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response_one.data['category_name'], self.category_data['category_name'])

    def test_api_can_get_single_category(self):
        """Test that the api can retrieve a category"""

        self.response_delete = self.client.delete(f'/blog/api/category/{self.response.data["id"]}/', format='json')

        self.assertEqual(self.response_delete.status_code, status.HTTP_204_NO_CONTENT)