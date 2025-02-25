import os
import json
import pytest
from src import Blob

TEST_FILE_DATA = "test_blob.bin"
TEST_KEY = "7f4cb1a49d668aa0d10fd66d5c0d940e"

@pytest.fixture
def blob():
    return Blob(key=TEST_KEY)

@pytest.fixture
def demo_data():
    demo_path = os.path.join(os.path.dirname(__file__), TEST_FILE_DATA)
    with open(demo_path, "r") as file:
        return file.read()

def test_static(blob):
    encrypted = blob.encrypt("Hello, World!")
    decrypted = blob.decrypt(encrypted)
    assert decrypted == "Hello, World!"

def test_decrypt_hcaptcha_generated(blob, demo_data):
    decrypted = blob.decrypt(demo_data)
    decrypted_json = json.loads(decrypted)

    assert len(decrypted_json) == 57