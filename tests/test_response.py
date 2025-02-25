import os
import pytest
from src import Response

TEST_FILE_RESPONSE = "test_response.bin"
KEY_DECRYPT = "6fac2cd349f10b851fbf9bf6af23c138de55ece30b1e9b94d98f5ffec2a393c2"

@pytest.fixture
def payload_decrypt():
    return Response(key=KEY_DECRYPT)

@pytest.fixture
def demo_data_response():
    demo_path = os.path.join(os.path.dirname(__file__), TEST_FILE_RESPONSE)
    with open(demo_path, "rb") as file:
        return file.read()

def test_decrypt_hcaptcha_generated(payload_decrypt, demo_data_response):
    decrypted = payload_decrypt.decrypt(demo_data_response)
    assert decrypted["request_config"]["version"] == 0