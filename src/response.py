from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import msgpack
import base64

class Response:
    def __init__(self, key: str) -> None:
        self.key: bytes = bytes.fromhex(key)

    def encrypt(self, data: dict) -> bytes:
        iv = get_random_bytes(12)
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)

        packed_data = msgpack.packb(data)
        encrypted, tag = cipher.encrypt_and_digest(packed_data)

        return iv + encrypted + tag

    def decrypt(self, data: str) -> dict:
        data = base64.b64decode(data)

        iv, encrypted_data, tag = data[:12], data[12:-16], data[-16:]
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)

        decrypted_data = cipher.decrypt_and_verify(encrypted_data, tag)
        return msgpack.unpackb(decrypted_data, strict_map_key=False)