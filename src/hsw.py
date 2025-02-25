from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import base64

class HSW:
    def __init__(self, key: str) -> None:
        self.key: bytes = bytes.fromhex(key)

    def encrypt(self, data: str) -> str:
        iv = get_random_bytes(12)
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)

        text, tag = cipher.encrypt_and_digest(data.encode())
        encrypted = text + tag + iv + b"\x00"

        return base64.b64encode(encrypted).decode()

    def decrypt(self, data: str) -> str:
        decoded = base64.b64decode(data)
        data, tag, iv = decoded[:-29], decoded[-29:-13], decoded[-13:][:-1]

        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)
        return cipher.decrypt_and_verify(data, tag).decode()