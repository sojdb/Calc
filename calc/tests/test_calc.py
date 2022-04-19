import numpy as np
from calc import derivative

class Testderivative:
    def test1(self):
        y = np.array([1,2,3])
        x = np.array([1,2,3])
        dydx = np.array([1.0,1.0])
        np.testing.assert_almost_equal(derivative(y,x), dydx)

    def test2(self):
        y = np.array([3,2,1])
        x = np.array([1,2,3])
        dydx = np.array([-1.0,-1.0])
        np.testing.assert_almost_equal(derivative(y,x), dydx)

    def test3(self):
        y = np.array([0,1,0])
        x = np.array([0, 1, 2])
        dydx = np.array([1.0, -1.0])
        np.testing.assert_almost_equal(derivative(y,x), dydx)
