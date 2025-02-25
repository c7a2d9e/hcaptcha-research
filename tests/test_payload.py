import json
import os
import pytest
from src import Payload

TEST_FILE_REQUEST = "test_payload.bin"
KEY_ENCRYPT = "0dab4adfafe851a03f225b2948a36cd064805d99e2a74b48135b869d9b3cd9c7"
EXPECTED_VERSION = "2382cc9b798791561b0dfdb2639870e37cbeb9fd"
EXPECTED_TYPE = "hsw"

@pytest.fixture
def payload_encrypt():
    return Payload(key=KEY_ENCRYPT)

@pytest.fixture
def demo_data_request():
    demo_path = os.path.join(os.path.dirname(__file__), TEST_FILE_REQUEST)
    with open(demo_path, "rb") as file:
        return file.read()

def test_static(payload_encrypt):
    encrypted = payload_encrypt.encrypt(
        data={
            "v": EXPECTED_VERSION,
            "sitekey": "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2",
        },
        site_config={
            "type": "hsw",
            "req": "eyJ0....",
        },
    )

    decrypted = payload_encrypt.decrypt(encrypted)
    assert decrypted[0]["v"] == EXPECTED_VERSION

def test_decrypt_hcaptcha_generated(payload_encrypt, demo_data_request):
    decrypted = payload_encrypt.decrypt(demo_data_request)
    site_config = json.loads(decrypted[1])
    assert site_config["type"] == EXPECTED_TYPE
