"""
Test custom Django management commands
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase, TestCase

from core.models import Employee

@patch('core.management.commands.wait_for_db.Command.check')
class CommandWaitForDBTests(SimpleTestCase):
    """Tests commands"""
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if tadabase is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    def test_wait_for_db_delay(self, patched_check):
        """Test waiting for database whith operationalError."""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

@patch('core.management.commands.generate_employees.Employee.objects.create')
class CommandGenerateEmployeeTests(TestCase):
    def test_generate_employees(self, mock_create):
        mock_create.return_value = Employee(
            full_name='Ralf Ringer',
            position='Level 1 manager',
            hire_date='2024-09-23',
            salary=50000,
            manager=None
        )
        call_command('generate_employees')
        expected_min = 50000
        self.assertTrue(mock_create.call_count >= expected_min)
