from widget import Widget
import unittest
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.wiget = Widget()
    def tearDown(self):
        self.wiget.dispose()
        self.wiget = None
    def testSize(self):
        self.assertEqual(self.wiget.getSize(),(40,40))
    def testResize(self):
        self.wiget.resize(100,100)
        self.assertEqual(self.wiget.getSize(),(1090,100))
if __name__ == "__main__":
    unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(WidgetTestCase("testSize"))
#     suite.addTest(WidgetTestCase("testResize"))
#     
#     runner = unittest.TextTestRunner()
#     runner.run(suite)