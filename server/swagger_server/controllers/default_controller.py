import connexion
import six

from swagger_server.models.employee import Employee  # noqa: E501
from swagger_server.models.employees_array import EmployeesArray  # noqa: E501
from swagger_server import util


def employee_uuid_delete(employee_uuid):  # noqa: E501
    """Delete an Employee with given UUID

    This endpoint will delete an existing Employee. # noqa: E501

    :param employee_uuid: UUID of a Employee
    :type employee_uuid: int

    :rtype: Employee
    """
    return 'do some magic!'


def employee_uuid_get(employee_uuid):  # noqa: E501
    """Get an Employee with given UUID.

    This endpoint returns a Employee from a given UUID. # noqa: E501

    :param employee_uuid: UUID of a Employee
    :type employee_uuid: int

    :rtype: Employee
    """
    return 'do some magic!'


def employee_uuid_put(employee_uuid, body):  # noqa: E501
    """Update an Employee with given UUID

    This endpoint will update an existing Employee. # noqa: E501

    :param employee_uuid: UUID of a Employee
    :type employee_uuid: int
    :param body: an Employee oject
    :type body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        body = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def root_get():  # noqa: E501
    """Get all Employees

    This endpoint returns a list of all Employees as an array. # noqa: E501


    :rtype: EmployeesArray
    """
    return 'do some magic!'


def root_post(body):  # noqa: E501
    """Create a new Employee

    This endpoint will create a new Employee. # noqa: E501

    :param body: an Employee oject
    :type body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        body = Employee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
