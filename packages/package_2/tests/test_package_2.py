import pytest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "horey", "common"))
from package_2 import __version__


def test_version():
    assert __version__ == "0.0.1"
