from base64 import urlsafe_b64encode, urlsafe_b64decode


def no_padding_b64encode(inp):
    return urlsafe_b64encode(inp).rstrip(b"=")


def no_padding_b64decode(inp):
    return urlsafe_b64decode(inp + (b"=" * (4 - (len(inp) % 4))))
