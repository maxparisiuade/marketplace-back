from botocore.exceptions import ClientError
from pydantic import BaseModel
import boto3

class DatabaseService():

    def __init__(self, table_name: str):
        self.table = boto3.resource('dynamodb').Table(table_name)

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
            return response.get('Item', None)
        except ClientError as e:
            print(f"Error getting item from DynamoDB: {e}")
            return None
    
    def get_all_items(self):
        try:
            response = self.table.scan()
            items = response.get('Items', [])
            return items
        except ClientError as e:
            print(f"Error getting all items from DynamoDB: {e}")
            return None
        
    def update_item(self, key: str, new_item: BaseModel):
        try:
            existing_item = self.get_item(key)
            
            if existing_item:
                updated_item = existing_item.copy()
                for key, value in new_item.items():
                    updated_item[key] = value

                print(updated_item)
                response = self.table.put_item(
                    Item=updated_item
                )
                return response
            else:
                print(f"Elemento con clave {key} no encontrado.")
                return None
        except ClientError as e:
            print(f"Error reemplazando el elemento en DynamoDB: {e}")
            return None
        
    def delete_item(self, key: str):
        try:
            response = self.table.delete_item(
                Key={
                    'uId': key
                }
            )
            return response
        except ClientError as e:
            print(f"Error eliminando el elemento de DynamoDB: {e}")
            return None