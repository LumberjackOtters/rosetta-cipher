from rosetta_cipher import cipher
import pytest


@pytest.mark.describe('version')
class TestRandom:

    @pytest.mark.it('returns version number')
    def test_version(self):
        version = cipher.get_version()
        assert version == "0.1.0"
        assert type(version) == str
