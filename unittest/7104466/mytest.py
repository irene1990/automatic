import sys
sys.path.append(r'../myclass.py')
import unittest
from myclass import myclass
class mytest(unittest.TestCase):
    def setUp(self):
        self.tclass = myclass()
    def tearDown(self):
        pass
    def testsum(self):
        myc = myclass()
        self.assertEqual(self.tclass.sum(1,2), 4)
    def testsub(self):
        myc = myclass()
        self.assertEqual(self.tclass.sub(2,1), 1, 'test sub fail')

if __name__=='__main__':
    unittest.main()