"""Tests for models."""

from django.test import TestCase
from core import models
from datetime import date


class ModelTest(TestCase):
    def test_create_employee(self):
        """Test creating employee."""
        employee = models.Employee.objects.create(
            full_name='Robert Downy-Jn',
            position='Chef-manager',
            hire_date=date(2024, 2, 12),
            salary=158000.00,
        )

        self.assertEqual(employee.full_name, str(employee))
