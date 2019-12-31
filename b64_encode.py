import base64
import sys


def base64Encode(text):
     '''encode utf-8 input to base 64'''
    return base64.standard_b64encode(bytes(text, 'utf-8')).decode('utf-8')


if __name__ == "__main__":
    text = sys.argv[1]
    print(base64Encode(text))
