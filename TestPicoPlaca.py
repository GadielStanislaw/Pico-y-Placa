import unittest
from Vehicle import Vehicle
from Verify import Verify
class TestPicoPlaca(unittest.TestCase):

    def testVerify(self):
        v = Vehicle('PCQ-1234','May 14 2019','19:28')
        r = Verify(v)
        #Test when time is between 7:00 to 9:30
        self.assertAlmostEqual(r.result(),'Warning this vehicle is not autorized for road')

        v_1 = Vehicle('PCQ-1234','May 12 2019','19:28')
        r_1 = Verify(v_1)
        #Test when date is weekend
        self.assertAlmostEqual(r_1.result(),'Ok this Vehicle is Autorized for road')

        v_2 = Vehicle('','','')
        r_2 = Verify(v_2)
        #Test when date is weekend
        self.assertAlmostEqual(r_2.result(),'There is not information about of Vehicle')