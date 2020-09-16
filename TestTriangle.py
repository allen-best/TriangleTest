# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testSetScalene(self): 
        self.assertEqual(classifyTriangle(10,25,30),'Scalene','10,15,30 is a Scalene triangle')
    
    def testSetIsoceles(self): 
        self.assertEqual(classifyTriangle(115,18,15),'Isoceles','15,18,15 is a Isoceles triangle')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(4,3,10),'NotATriangle','4,3,10 is not a triangle')
        
    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(4.5,3.3,10.1),'InvalidInput','4.5,3.3,10.1 should be InvalidInput')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

