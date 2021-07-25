from cvapps_sol1_checker import Solution
import numpy as np

import pytest


def test_find_panorama_shape():
    sol = Solution()
    assert (sol.compute_homography_naive(
        np.random.rand(2, 20), np.random.rand(2, 20)) == np.ones((3, 3))).all()
