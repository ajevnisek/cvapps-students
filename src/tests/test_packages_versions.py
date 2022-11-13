from ..cvapps_sol1_checker import *
import pytest



def test_matplotlib_version():
    assert (matplotlib.__version__ == '3.4.3')


def test_numpy_version():
    assert (np.__version__ == '1.23.4')

def test_tqdm_version():
    assert (tqdm.__version__ == '4.64.1')

