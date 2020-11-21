from rosetta_cipher import cipher
import pytest


@pytest.mark.parametrize("obj", ["Hello", "v1.2.3", "v1.2.3-alpha-rc", 2])
@pytest.mark.parametrize("length", [1, 2, 3, 5, 7])
@pytest.mark.parametrize("retry", [0, 1])
@pytest.mark.parametrize("separator", ["_", "."])
@pytest.mark.parametrize("capitalize", [False, True])
@pytest.mark.describe("random")
class TestName:
    @pytest.mark.it("test type for {obj}_{length}_{retry}_{separator}_{capitalize}")
    def test_random(self, obj, length, retry, separator, capitalize):
        assert (
            type(
                cipher.get_name(
                    obj=obj,
                    length=length,
                    retry=retry,
                    separator=separator,
                    capitalize=capitalize,
                )
            )
            == str
        )

    @pytest.mark.it("test retry for {obj}_{length}_{retry}_{separator}_{capitalize}")
    def test_retry(self, obj, length, retry, separator, capitalize):
        rand = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        name = cipher.get_name(
            obj=obj,
            length=length,
            retry=retry,
            separator=separator,
            capitalize=capitalize,
        )
        last = name.split(separator)[len(name.split(separator)) - 1]
        assert type(last) == str
        if retry > 0:
            assert last in rand

    @pytest.mark.it(
        "test separator for {obj}_{length}_{retry}_{separator}_{capitalize}"
    )
    def test_separator(self, obj, length, retry, separator, capitalize):
        name = cipher.get_name(
            obj=obj,
            length=length,
            retry=retry,
            separator=separator,
            capitalize=capitalize,
        )
        if length > 1:
            assert separator in name
        full_length = length - 1
        full_length = full_length + 1 if retry > 0 else full_length

        assert name.count(separator) == full_length

    @pytest.mark.it(
        "test capitalize for {obj}_{length}_{retry}_{separator}_{capitalize}"
    )
    def test_capitalize(self, obj, length, retry, separator, capitalize):
        name = cipher.get_name(
            obj=obj,
            length=length,
            retry=retry,
            separator=separator,
            capitalize=capitalize,
        )
        if capitalize:
            assert name.isupper()
        else:
            assert name.islower()

    @pytest.mark.it("test length for {obj}_{length}_{retry}_{separator}_{capitalize}")
    def test_length(self, obj, length, retry, separator, capitalize):
        name = cipher.get_name(
            obj=obj,
            length=length,
            retry=retry,
            separator=separator,
            capitalize=capitalize,
        )
        assert len(name.split(separator)) == length if retry == 0 else length + 1
