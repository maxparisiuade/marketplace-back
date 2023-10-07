from botocore.exceptions import ClientError
from ..db.db import initialize_db
from pydantic import BaseModel


class DatabaseService():

    def __init__(self, table_name: str):
        self.table = initialize_db().Table(table_name)

    def add_item(self, item: BaseModel):
        try:
            response = self.table.put_item(
                Item=item.dict()
            )
            return response
        except ClientError as e:
            print(f"Error adding item to DynamoDB: {e}")
            return None
        
    def get_item(self, key: str):
        try:
            response = self.table.get_item(
                Key={
                    'uId': key
                }
            )
            print(response)
            return response
        except ClientError as e:
            print(f"Error getting item from DynamoDB: {e}")
            return None