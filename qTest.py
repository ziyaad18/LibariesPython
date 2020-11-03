import unittest


class learnUnitTest(unittest.TestCase):
    def sampleTest(self):
        num1 = 5
        num2 = 5

        self.assertEqual(num1,num2,"they are equal")
if __name__ == '__main__':
    unittest.main()