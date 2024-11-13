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
Run either the confluent-kafka-python library or kafka-python library to produce messages
```
python3 confluent_kafka_entrypoint.py
```
Or
```
python3 kafka_entrypoint.py
```