# -*- coding:utf-8 -*-
# writen by ChuanyuXue

import numpy

class mvtest:
    def __init__(self):
        self._n = None
        self._m = None
        self.quantiles = [
            [0.1178, 0.2091, 0.2442, 0.2860, 0.3469, 0.4665, 0.4968, 0.5416, 0.5984, 0.7120],
            [0.2773, 0.4227, 0.4631, 0.5220, 0.6086, 0.7365, 0.7776, 0.8377, 0.9278, 1.0673],
            [0.4385, 0.6231, 0.6761, 0.7495, 0.8384, 0.9938, 1.0453, 1.1055, 1.2090, 1.3393],
            [0.6028, 0.8158, 0.8737, 0.9519, 1.0602, 1.2399, 1.2911, 1.3622, 1.4408, 1.6026],
            [0.7694, 1.0097, 1.0786, 1.1670, 1.2698, 1.4440, 1.4955, 1.5776, 1.6992, 1.8650],
            [0.9423, 1.2035, 1.2757, 1.3627, 1.4927, 1.6986, 1.7672, 1.8268, 1.9691, 2.1241],
            [1.0971, 1.3787, 1.4569, 1.5549, 1.6780, 1.8901, 1.9581, 2.0594, 2.1693, 2.3645],
            [1.2708, 1.5774, 1.6674, 1.7672, 1.8963, 2.1096, 2.1742, 2.2597, 2.3809, 2.6180],
            [1.4468, 1.7812, 1.8707, 1.9773, 2.1019, 2.3362, 2.4081, 2.5011, 2.6215, 2.7943]
        ]
        self.prob = [0.50, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99]

    def _f(self, s, x):
        return len(x[x <= s]) / self._n

    def _fr(self, s, t, x, y):
        return len(x[(x <= s) & (y == t)]) / len(y[y == t])

    def _pr(self, t, y):
        return len(y[y == t]) / self._n

    def _quantiles_transformer(self, result):
        quantiles = self.quantiles[self._m - 2]
        if result < quantiles[0]:
            return [0.50, 1]
        if quantiles[len(quantiles) - 1] <= result:
            return [0, 0.01]
        for i in range(len(quantiles) - 1):
            if quantiles[i] <= result < quantiles[i+1]:
                return [round(1-self.prob[i+1], 2), round(1-self.prob[i], 2)]

    def test(self, x: numpy.ndarray, y: numpy.ndarray)->dict:
        try:
            x = numpy.array(x)
        except Exception:
            raise Exception("The expected type of this argument is Array or List,"
                            " however \"" + str(type(x)) + "\" is gotten.")
        try:
            y = numpy.array(y, dtype=int)
        except Exception:
            raise Exception("The expected type of this argument is Array or List,"
                            " however \"" + str(type(y)) + "\" is gotten.")
        if len(x) == 0 or len(y) == 0:
            raise Exception("The input vectors cannot be empty.")
        if type(x.dtype) == str or type(y.dtype) == str:
            raise Exception("The element type of input vectors cannot be \"str\".")

        self._n = len(x)
        self._m = len(numpy.unique(y))

        if self._n == len(y):
            result = 0
            for t in numpy.unique(y):
                pr = self._pr(t, y)
                for s in x:
                    result += pr * numpy.square(self._fr(s, t, x, y) - self._f(s, x))
            return {'Tn': round(result, 2), 'p-value': self._quantiles_transformer(result)}
        else:
            raise Exception("Two vectors must be equal to the same dimension vector.")



















