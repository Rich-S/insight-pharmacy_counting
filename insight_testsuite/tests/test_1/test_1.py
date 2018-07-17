import unittest
import pythoncode

location  = './input/itcont.txt'
test_drug = 'CLINDAMYCIN HCL'

class TestCalc(unittest.TestCase):
    def test_nsubs(self):
        result1, result2 = pythoncode.summarize(location,test_drug)
        self.assertEqual(result1,1)
        print(test_drug + " has " + str(result1) + " unique prescriber")

    def test_totalcost(self):
        result1, result2 = pythoncode.summarize(location,test_drug)
        self.assertEqual(result2,113.07)
        print(test_drug + " has a total cost of " + str(result2)) 
                                     

if __name__=="__main__":
    unittest.main()

