# if you want to use IAM, uncomment #

from kafka import KafkaProducer
#from producer.msk_token_provider_for_kafka_python import MSKTokenProvider
from config.settings import Settings


class KafkaProducerClient:
    def __init__(self):
#        tp = MSKTokenProvider()
        self.producer = KafkaProducer(
            bootstrap_servers=Settings.BOOTSTRAP_SERVERS,
            sasl_mechanism='SCRAM-SHA-512',
            sasl_plain_username='admin',
            sasl_plain_password='admin',
            security_protocol='SASL_SSL',
            api_version=(3,6,0)
#            sasl_mechanism='OAUTHBEARER',
#            sasl_oauth_token_provider=tp,
#            client_id=tp.get_client_id()
        )

    def send_message(self, topic, message) -> None:
        try:
            self.producer.send(topic, value=message)
            self.producer.flush()
            print("Produced!")
        except Exception as e:
            print("Failed to send message:", e)

    def close(self) -> None:
        self.producer.close()
