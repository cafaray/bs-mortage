# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.employee import Employee  # noqa: E501
from swagger_server.models.employees_array import EmployeesArray  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_employee_uuid_delete(self):
        """Test case for employee_uuid_delete

        Delete an Employee with given UUID
        """
        response = self.client.open(
            '/v1/employees/{employee-uuid}'.format(employee_uuid=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employee_uuid_get(self):
        """Test case for employee_uuid_get

        Get an Employee with given UUID.
        """
        response = self.client.open(
            '/v1/employees/{employee-uuid}'.format(employee_uuid=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employee_uuid_put(self):
        """Test case for employee_uuid_put

        Update an Employee with given UUID
        """
        body = Employee()
        response = self.client.open(
            '/v1/employees/{employee-uuid}'.format(employee_uuid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        Get all Employees
        """
        response = self.client.open(
            '/v1/employees/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_post(self):
        """Test case for root_post

        Create a new Employee
        """
        body = Employee()
        response = self.client.open(
            '/v1/employees/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
