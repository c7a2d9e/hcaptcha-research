import json
import os
import pytest
from src import HSW

TEST_FILE_NAME = "test_hsw.bin"
TEST_KEY = "6ae4cf1ff85e739dcbfc9cfc92efa5829975a2c81a32652d78e35b9a7fd0a8cc"
EXPECTED_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"

@pytest.fixture
def hsw_instance():
    return HSW(key=TEST_KEY)

@pytest.fixture
def demo_data():
    demo_path = os.path.join(os.path.dirname(__file__), TEST_FILE_NAME)
    with open(demo_path, "r") as file:
        return file.read()

def test_static(hsw_instance):
    encrypted = hsw_instance.encrypt("Hello, World!")
    decrypted = hsw_instance.decrypt(encrypted)
    assert decrypted == "Hello, World!"

def test_decrypt_hcaptcha_generated(hsw_instance, demo_data):
    decrypted = hsw_instance.decrypt(demo_data)
    decrypted_json = json.loads(decrypted)

    assert decrypted_json["components"]["navigator"]["user_agent"] == EXPECTED_USER_AGENT