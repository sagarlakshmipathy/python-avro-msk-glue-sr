import socket
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider


class MSKTokenProvider:
    @staticmethod
    def token() -> tuple:
        token, expiry_ms = MSKAuthTokenProvider.generate_auth_token('us-west-2')
        return token

    @staticmethod
    def get_client_id() -> str:
        return socket.gethostname()
