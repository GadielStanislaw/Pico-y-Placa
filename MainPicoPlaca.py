from Verify import Verify
from Vehicle import Vehicle
from datetime import time
if __name__ == '__main__':
    v = Vehicle('PCQ-1234','May 14 2019','19:28')
    r = Verify(v)
    r.result()

    #Unit Test 
    vehiclesData=[('PCQ-1234','May 14 2019','19:28'), 
    ('PCQ-1234','May 14 2019','20:28'), 
    ('PCQ-1234','May 14 2019','7:00'), 
    ('PCQ-1234','May 14 2019','9:00'),
    ('PCQ-1236','May 14 2019','9:00'),
    ('PCQ-1236','May 15 2019','7:10'),
    ('PCQ-1236','May 14 2019','19:28'), 
    ('','','')]
    for vTest in vehiclesData:
        vTestAux=Vehicle(vTest[0], vTest[1], vTest[2])
        r = Verify(vTestAux)
        r.result()
