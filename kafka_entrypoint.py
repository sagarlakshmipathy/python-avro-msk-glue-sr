from config.settings import Settings
from producer.kafka_producer import KafkaProducerClient
from schema_registry.registry_client import GlueSchemaRegistry
from aws_schema_registry.avro import AvroSchema
from aws_schema_registry import DataAndSchema
from aws_schema_registry.adapter.kafka import KafkaSerializer
from utils.file_reader import FileReader

# Read schema
schema_str = FileReader.read_file(Settings.SCHEMA_FILE)

# Initialize Glue Schema Registry and create schema
registry_client = GlueSchemaRegistry()
registry_client.create_registry_and_schema(Settings.SCHEMA_NAME, schema_str)

# Read data
data = FileReader.read_json(Settings.DATA_FILE)

# Initialize serializer
serializer = KafkaSerializer(registry_client.client)


# Serialize message
def serialize_avro(message) -> bytes:
    avro_schema = AvroSchema(schema_str)
    data_and_schema = DataAndSchema(data=message, schema=avro_schema)
    return serializer.serialize(Settings.SCHEMA_NAME, data_and_schema)


# Produce message
producer_client = KafkaProducerClient()
try:
    avro_message = serialize_avro(data)
    producer_client.send_message(Settings.TOPIC, avro_message)
finally:
    producer_client.close()
