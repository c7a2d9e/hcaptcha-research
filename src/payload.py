from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import json
import msgpack

class Payload:
    def __init__(self, key: str) -> None:
        self.key: bytes = bytes.fromhex(key)

    def encrypt(self, data: dict, site_config: dict) -> bytes:
        config = json.dumps(site_config, separators=(',', ':'))

        iv = get_random_bytes(12)
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)

        enc, checksum = cipher.encrypt_and_digest(msgpack.packb(data))
        encrypted_data = msgpack.ExtType(18, iv + enc + checksum)

        return msgpack.packb([config, encrypted_data])

    def decrypt(self, data: bytes) -> tuple:
        unpacked = msgpack.unpackb(data, strict_map_key=False)
        config, encrypted_data = unpacked

        iv = encrypted_data.data[:12]
        enc = encrypted_data.data[12:-16]
        tag = encrypted_data.data[-16:]

        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)
        decrypted_data = cipher.decrypt_and_verify(enc, tag)

        return msgpack.unpackb(decrypted_data, strict_map_key=False), config