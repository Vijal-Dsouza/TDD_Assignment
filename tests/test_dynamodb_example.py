import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import boto3
import pytest
from moto import mock_aws
from src.boto3_example import DynamodBExample

db_instance = DynamodBExample()
table_name = "Movies"

@pytest.fixture
def dynamodb():
    with mock_aws():
        yield boto3.resource('dynamodb',region_name='us-east-1')


def test_create_dynamo_table(dynamodb):
    '''
        Implement the test logic here for testing create_dynamo_table method
    '''
    
    table = db_instance.create_movies_table()
    table_from_mock = dynamodb.Table(table_name)

    assert table_from_mock.table_name == table_name


# @mock_dynamodb2
# def test_add_dynamo_record_table():
#     '''
#         Implement the test logic here for testing add_dynamo_record_table method
#     '''
#     assert False

# @mock_dynamodb2
# def test_add_dynamo_record_table_failure():
#     '''
#         Implement the test logic here test_add_dynamo_record_table method for failures
#     '''
#     assert False
