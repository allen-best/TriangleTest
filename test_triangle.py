# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle_check import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral')

    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(10,25,30),'Scalene')
    
    def testIsocelesTriangle(self): 
        self.assertEqual(classify_triangle(15,18,15),'Isoceles')

    def testNotATriangle(self): 
        self.assertEqual(classify_triangle(4,3,10),'NotATriangle')
        
    def testInvalidInput(self): 
        self.assertEqual(classify_triangle(4.5,3.3,10.1),'InvalidInput')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

