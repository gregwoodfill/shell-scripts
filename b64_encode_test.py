from b64_encode import base64Encode


def test_encodes_in_base64():
    expected = "aGVsbG8gd29ybGQ="

    # when
    encoded = base64Encode("hello world")

    assert encoded == expected
