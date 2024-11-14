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

## Check connectivity
```
[ec2-user@ip-172-31-8-99 python-avro-msk-glue-sr]$ nc -zv b-2.onehouse.5tpo0i.c8.kafka.us-west-2.amazonaws.com 9098
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Connected to 172.31.46.118:9098.
Ncat: 0 bytes sent, 0 bytes received in 0.40 seconds.
```

## Create topic
MSK doesn't automatically create a topic.  Create the topic or else your client will just hang. 

## Run the producer
Run producers from either `confluent-kafka-python` library or `kafka-python` library to produce messages
```
python3 confluent_kafka_entrypoint.py
```
or
```
python3 kafka_entrypoint.py
```
