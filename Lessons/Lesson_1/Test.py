import pytest
import os
from Exercise import get_current_working_directory, decode_string, encode_string

def test_current_working_directory():
    assert os.getcwd() == get_current_working_directory()

@pytest.mark.parametrize("encoded,decoded", [
    ("UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSEgQXMgaXMgQysr",
     "Python is a cool programming language! As is C++"),
    ("V2l0aCBlbm91Z2ggZXllcyBhbGwgYnVncyBhcmUgc2hhbGxvdw==",
     "With enough eyes all bugs are shallow"),
    ("UHJvZ3JhbSB0ZXN0aW5nIGNhbiBiZSB1c2VkIHRvIHNob3cgdGhlIHByZXNlbmNlIG9mIGJ1Z3MsIGJ1dCBuZXZlciB0byBzaG93IHRoZWlyIGFic2VuY2UhIFBsZWFzZSBkb24ndCBmYWxsIGludG8gdGhlIHRyYXAgb2YgYmVsaWV2aW5nIHRoYXQgSSBhbSB0ZXJyaWJseSBkb2dtYXRpY2FsIGFib3V0IFt0aGUgZ290byBzdGF0ZW1lbnRdLg==",
     "Program testing can be used to show the presence of bugs, but never to show their absence! Please don't fall into the trap of believing that I am terribly dogmatical about [the goto statement].")
])
def test_decode_string(encoded, decoded):
    assert decode_string(encoded) == decoded, f"Failed to decode string {encoded}"

@pytest.mark.parametrize("decoded,encoded", [
    ("Python is a cool programming language! As is C++",
     "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSEgQXMgaXMgQysr"),
    ("With enough eyes all bugs are shallow",
     "V2l0aCBlbm91Z2ggZXllcyBhbGwgYnVncyBhcmUgc2hhbGxvdw=="),
    ("Program testing can be used to show the presence of bugs, but never to show their absence! Please don't fall into the trap of believing that I am terribly dogmatical about [the goto statement].",
     "UHJvZ3JhbSB0ZXN0aW5nIGNhbiBiZSB1c2VkIHRvIHNob3cgdGhlIHByZXNlbmNlIG9mIGJ1Z3MsIGJ1dCBuZXZlciB0byBzaG93IHRoZWlyIGFic2VuY2UhIFBsZWFzZSBkb24ndCBmYWxsIGludG8gdGhlIHRyYXAgb2YgYmVsaWV2aW5nIHRoYXQgSSBhbSB0ZXJyaWJseSBkb2dtYXRpY2FsIGFib3V0IFt0aGUgZ290byBzdGF0ZW1lbnRdLg==")
])
def test_encode_string(decoded, encoded):
    assert encode_string(decoded) == encoded, f"Failed to encode string {decoded}"