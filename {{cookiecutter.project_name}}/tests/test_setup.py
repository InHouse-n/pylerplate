from src import __version__ as version


def test_version(fake):
    assert version == "1.0.0"
    assert fake.pystr() != version
