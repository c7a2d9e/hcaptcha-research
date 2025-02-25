from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64

class Blob:
    def __init__(self, key: str) -> None:
        self.key: bytes = bytes.fromhex(key)

    def decrypt(self, data: str) -> str:
        iv, ciphertext = map(base64.b64decode, data.split('.'))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted.decode('utf-8')

    def encrypt(self, data: str) -> str:
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(iv).decode() + '.' + base64.b64encode(encrypted).decode()