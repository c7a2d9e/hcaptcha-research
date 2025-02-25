# hCaptcha Research
Research relating to [hCaptcha](https://hcaptcha.com)'s encryption methods.
If you're looking for paid commissions based around hCaptcha or wish to purchase up-to-date keys, contact me at [work@sys32.dev](mailto://work@sys32.dev)

> [!NOTE]
> hCaptcha's encryption key(s) and blob key can change.
> The keys are dynamic for each `hsw.js` version.
> We used the keys from [`9124ffd8f5f2c6e337d7bca9aebb40fbdb78dde420f3e6b156b820445bf3d1a2`](https://newassets.hcaptcha.com/c/9124ffd8f5f2c6e337d7bca9aebb40fbdb78dde420f3e6b156b820445bf3d1a2/hsw.js) in this demo.

## Encryptions
Short description of each encryption.

### HSW
hCaptcha's `hsw` payload is the main payload being sent when you execute the `get_captcha` request.
It contains all the fingerprint data required for hCaptcha to validate.
Example usage can be found inside: [`tests/test_hsw.py`](tests/test_hsw.py).

### Blob
hCaptcha's `blob` can be found inside the decrypted `HSW` payload named `fingerprint_blob`.
It contains various fingerprint information & hashes.
Example usage can be found inside: [`tests/test_blob.py`](tests/test_blob.py).

### Payload
This encryption is used if the hCaptcha site uses `enc_get_req` feature.
It is used for encrypting the request you're sending to hCaptcha.
Example usage can be found inside: [`tests/test_payload.py`](tests/test_payload.py).

### Response
This encryption is used once again if `enc_get_req` feature is enabled.
It is used to decrypt the response you get back from hCaptcha.
Example usage can be found inside: [`tests/test_response.py`](tests/test_response.py).

# Acknowledgements
The Python implementations inside [`src/*`](src/__init__.py) are written by an unknown source.

# Legal Disclaimer
This repository is intended for educational and research purposes only. The code and content provided here are not affiliated with, endorsed by, or associated with [hCaptcha](https://www.hcaptcha.com) or any related entities.

If you are a representative of hCaptcha and believe this repository violates your rights or terms of service, please contact me at [**legal@sys32.dev**](mailto://legal@sys32.dev) to request its removal. I will respond promptly to resolve the issue.