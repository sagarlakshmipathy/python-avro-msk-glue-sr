from confluent_kafka import Producer
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
from config.settings import Settings
import socket


class ConfluentKafkaProducerClient:
    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': Settings.BOOTSTRAP_SERVERS,
            'security.protocol': 'SASL_SSL',
            'sasl.mechanisms': 'OAUTHBEARER',
            'oauth_cb': self._oauth_callback,
            'client.id': socket.gethostname(),
        })

    def _oauth_callback(self, config_str: str) -> tuple[str, float]:
        """
        OAuth callback that generates AWS MSK IAM authentication token.
        Returns tuple of (token, expiration_time_in_seconds)
        """
        try:
            token, expiry_ms = MSKAuthTokenProvider.generate_auth_token('us-west-2')
            # Convert expiry from milliseconds to seconds
            expiry_seconds = expiry_ms / 1000.0
            return token, expiry_seconds
        except Exception as e:
            print(f"Failed to generate auth token: {e}")
            raise

    def send_message(self, topic: str, message: bytes) -> None:
        try:
            self.producer.produce(topic, value=message)
            self.producer.flush()
            print("Produced!")
        except Exception as e:
            print("Failed to send message:", e)

    def cleanup(self, timeout: float = 30.0) -> None:
        """
        Flush any pending messages and cleanup resources.
        """
        try:
            remaining = self.producer.flush(timeout)
            if remaining > 0:
                print(f"Warning: {remaining} messages were not delivered within timeout period")
        except Exception as e:
            print(f"Error during cleanup: {e}")