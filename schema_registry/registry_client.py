import boto3
import botocore.exceptions
from aws_schema_registry import SchemaRegistryClient
from config.settings import Settings


class GlueSchemaRegistry:
    def __init__(self):
        session = boto3.Session(region_name=Settings.REGION)
        self.glue_client = session.client('glue')
        self.client = SchemaRegistryClient(self.glue_client, registry_name=Settings.REGISTRY_NAME)

    def create_registry_and_schema(self, schema_name, schema_str) -> None:
        try:
            self.glue_client.create_registry(RegistryName=Settings.REGISTRY_NAME)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'AlreadyExistsException':
                raise e

        try:
            self.glue_client.create_schema(
                RegistryId={"RegistryName": Settings.REGISTRY_NAME},
                SchemaName=schema_name,
                DataFormat="AVRO",
                Compatibility="BACKWARD",
                SchemaDefinition=schema_str
            )
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'AlreadyExistsException':
                raise e
