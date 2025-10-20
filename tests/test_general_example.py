from src.general_example import GeneralExample
import pytest

general_example_instance = GeneralExample()

def test_flatten_dictionary():
    text = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
    expected = [0, 1, 2, 3, 10, 22, 42, 55]

    actual = general_example_instance.flatten_dictionary(text)
    assert expected == actual

def test_load_employee_rec_from_database(mocker):

    mock_func = mocker.patch('src.general_example.GeneralExample.load_employee_rec_from_database')
    mock_func.return_value = ['emp001', 'Sam', '100000']

    expected = ['emp001', 'Sam', '100000']
    actual = general_example_instance.load_employee_rec_from_database()

    assert actual == expected

def test_fetch_emp_details(mocker):
    mock_func = mocker.patch('src.general_example.GeneralExample.fetch_emp_details')
    mock_func.return_value = {'empId':'emp001',
            'empName': 'Sam',
            'empSalary': '100000'}

    expected = {'empId':'emp001',
            'empName': 'Sam',
            'empSalary': '100000'}
    actual = general_example_instance.fetch_emp_details()

    assert actual == expected
