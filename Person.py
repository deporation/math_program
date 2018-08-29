# Persona.py
import numpy as np
import random
P = [[0.5, 0.4,0.1],
     [0.2,0.7,0.1],
     [0.4,0.2,0.4]]
arr2 = np.array(P)
ran = random.random()
class Person :
    val = 1
    def __init__(self,value):
        self.val = value
    def last(self,count):
        for i in range(0,count):
            temp = -1
            r = random.random()
            if r < arr2[self.val][0]:
                temp=0
            elif r < arr2[self.val][0]+arr2[self.val][1]:
                temp = 1
            else:
                temp = 2
            self.val = temp
    def get_value (self):
        return self.val