from Task2.log import *

class ineuron_courses:
    lp.info("Class is invoked")
    try:
        def __init__(self, course1, course2, course3):
            self.course1 = course1
            self._course2 = course2
            self.__course3 = course3
            lp.info("The input value is declared in the function" + str(self.course1)+"," + str(self._course2) + " and " + str(self.__course3))
        def courses(self):
            print("The courses offerred by ineuron are: {}, {} and {}".format(self.course1, self._course2,self.__course3))
            lp.info("Function execution success")
        def modify(self,k):
            self.__course3 = k
            lp.info("The new value is"+ str(self.__course3))
            lp.info("function completed success")
        def No_of_courses(self,k):
            print("The number of courses in ineuron is {}".format(k))
            lp.info("The number of courses in ineuron is" + str(k))
    except Exception as e:
        print(e)
        lp.error(e)

class one_neuron:
    lp.info("class is invoked")
    try:
        def __init__(self, course1, course2, course3):
            self.course1 = course1
            self._course2 = course2
            self.__course3 = course3
            lp.info("The input value is declared in the function" + str(self.course1) + "," + str(self._course2) + " and " + str(self.__course3))
        def courses(self):
            print("The one_neuron courses from ineuron are: {}, {} and {}".format(self.course1, self._course2, self.__course3))
            lp.info("Function completed")
    except Exception as e:
        print(str(e))
        lp.error(e)

# multiple inheritance
class ineuron_affiliates_market_courses(ineuron_courses, one_neuron):
    lp.info("class is invoked")
    try:
        def __init__(self, course1, course2, course3):
            self.course1 = course1
            self._course2 = course2
            self.__course3 = course3
            lp.info("The input value is declared in the function" + str(self.course1) + "," + str(self._course2) + " and " + str(self.__course3))
        def __courses(self):
            print("The affiliates marketing courses from ineuron are: {}, {} and {}".format(self.course1, self._course2, self.__course3))
            lp.info("Function completed")
    except Exception as e:
        print(str(e))
        lp.error(e)