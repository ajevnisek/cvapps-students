from ..cvapps_sol1_checker import *
import pytest


def test_cv2_version():
    assert(cv2.__version__ == '4.5.2')

def test_matplotlib_version():
    assert (matplotlib.__version__ == '3.5.1')


def test_numpy_version():
    assert (np.__version__ == '1.21.1')

# def test_tqdm_version():
#     assert (tqdm.__version__ == '4.64.1')

