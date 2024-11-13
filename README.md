## Description
This project is a simple example of how to produce messages (AVRO format) to a Kafka topic in Amazon MSK using the `confluent-kafka-python` library and the `kafka-python` library and register to AWS Glue Schema Registry.

## Setup
1. Start a virtualenv
```
python3 -m venv sc-ingest
source sc-ingest/bin/activate
```

2. Install the required libraries
```
python3 -m pip install -r requirements.txt
```

## Run the producer
Run producers from either `confluent-kafka-python` library or `kafka-python` library to produce messages
```
python3 confluent_kafka_entrypoint.py
```
or
```
python3 kafka_entrypoint.py
```
