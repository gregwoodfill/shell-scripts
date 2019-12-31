import sys
import base64


def decodeBase64(text: str):
    '''decode utf-8 input to base 64'''
    txt_bytes = text.encode('utf-8')
    return base64.standard_b64decode(txt_bytes).decode('utf-8')


if __name__ == "__main__":
    print(decodeBase64(sys.argv[1]))
