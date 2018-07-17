import unittest
import pythoncode

location  = './input/itcont.txt'

class TestCalc(unittest.TestCase):
    def test_nsubs(self):
        result1, result2 = pythoncode.summarize(location)
        self.assertEqual(result1,1)
        print("Only " + str(result1) + " unique prescriber - his name is Amir")

    def test_totalcost(self):
        result1, result2 = pythoncode.summarize(location)
        self.assertEqual(result2,81124.05)
        print("Amir has a total cost of " + str(result2)) 
                                     

if __name__=="__main__":
    unittest.main()
