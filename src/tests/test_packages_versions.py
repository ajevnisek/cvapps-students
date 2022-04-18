from ..cvapps_sol1_checker import *
import pytest


def test_cv2_version():
    assert (cv2.__version__ == '4.5.4')


def test_matplotlib_version():
    assert (matplotlib.__version__ == '3.4.3')


def test_numpy_version():
    assert (np.__version__ == '1.20.3')
