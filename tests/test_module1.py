#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

"""Docstrings for the unittest."""


import sys
sys.path.insert(0, '/Users/lorenzomarini/Desktop/package1')
# REASON: https://bic-berkeley.github.io/psych-214-fall-2016/sys_path.html
#for path in sys.path:
#    print(path)

import unittest


from package1.module1 import func1
# ALTERNATIVA (meno bella)
#sys.path.insert(0, '/Users/lorenzomarini/Desktop/package1')
#from module1 import function1

class TestFunc1(unittest.TestCase):
    """Unittest for the module1 module"""

    def test_int(self):
        """Test with integers"""
        self.assertAlmostEqual(func1(2, 2), 4) 
        # https://docs.python.org/3/library/unittest.html
        # assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)
        # Checks that: round(first - secondo, 7) == 0

        # Verifica che il primo (func1(2,2)) e il secondo (4) 
        # siano approssimativamente (o non approssimativamente) 
        # uguali calcolando la differenza,
        # arrotondando al numero dato di cifre decimali (predefinito 7) 
        # e confrontando a zero. Si noti che questi metodi arrotondano 
        # i valori al numero di cifre decimali specificato (cioè come 
        # la funzione round ()) e cifre non significative.

        # Se viene fornito delta al posto delle posizioni, 
        # la differenza tra il primo e il secondo deve essere 
        # minore o uguale a (o maggiore di) delta.
    
    def test_float(self):
        """Test with floats"""
        self.assertAlmostEqual(func1(2.5, 2.5), 5.0) 


if __name__ == "__main__":
    unittest.main()




