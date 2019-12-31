import sys
import base64


def decodeBase64(text: str):
    txt_bytes = text.encode('utf-8')
    return base64.standard_b64decode(txt_bytes).decode('utf-8')
