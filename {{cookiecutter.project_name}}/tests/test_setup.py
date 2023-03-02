from example import __version__ as version

from {{cookiecutter.package_name}} import __version__ as version


def test_version(fake):
    """Sanity check that there is a version in the right place"""
    assert version == "1.0.0"
    assert fake.pystr() != version
