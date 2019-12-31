from b64_decode import decodeBase64


def test_decode():
    expected = 'hello world'

    # when
    actual = decodeBase64("aGVsbG8gd29ybGQ=")

    # then
    assert actual == expected
