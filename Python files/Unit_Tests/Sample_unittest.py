__author__ = 'myth'


import unittest

class SampleTest(unittest.TestCase):

    def setUp(self):   # This is file where initial variables that can be used in the test methods can be defined
        print 'setUp: Start'
        self.variable1=1
        self.variable2=2
        print 'setUp: End'

    def test1(self):   # First test function
        print 'test1: Begin'
        self.assertNotEqual(self.variable1,self.variable2,'A message can be put here in case the test fails')
        print 'test1: End'

    def test2(self):   # Second test function
        print 'test2: Begin'
        self.assertGreater(self.variable1,self.variable2)
        print 'test2: End'

    def tearDown(self): # Here the variables initialised can be reset for the next test
        print 'tearDown: Start'
        self.variable1=0
        self.variable2=0
        print 'tearDown: End'

if __name__=='__main__':
    unittest.main()

