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
    mock_table = dynamodb.Table(table_name)

    assert mock_table.table_name == table_name


def test_add_dynamo_record_table(dynamodb):
    '''
        Implement the test logic here for testing add_dynamo_record_table method
    '''
    item = {
        'year': 2025,
        'title': 'Success',
    }
    db_instance.create_movies_table()
    db_instance.add_dynamo_record(table_name, item)
    table = dynamodb.Table(table_name)
    
    assert table.item_count == 1


def test_add_dynamo_record_table_failure(dynamodb):
    '''
        Implement the test logic here test_add_dynamo_record_table method for failures
    '''
    item = {
        'year': 2025,
    }
    db_instance.create_movies_table()
    with pytest.raises(Exception) as exec_type:
        db_instance.add_dynamo_record(table_name,item)
    assert "Validation Exception" in exec_type.value.args[0]
