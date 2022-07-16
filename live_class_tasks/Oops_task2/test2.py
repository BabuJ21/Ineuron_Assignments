## packages and modules
from module_test.test3 import *
from Task2.test1 import *
from Task2.log import *

class ineuron_products:
    lp.info("Class is invoked")
    try:
        def __init__(self, product1, product2, product3, product4):
            self.product1 = product1
            self.product2 = product2
            self.product3 = product3
            self.product4 = product4
            lp.info("Input values are added")
        def products(self):
            print("The products of ineuron are: {}, {} and {}".format(self.product1, self.product2, self.product3, self.product4))
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))

class ineuron_live_class_batches:
    lp.info("Class is invoked")
    try:
        def __init__(self, batch1, batch2, batch3, batch4):
            self.batch1 = batch1
            self.batch2 = batch2
            self.batch3 = batch3
            self.batch4 = batch4
            lp.info("Input values added")
        def batches(self):
            print("The tech batches of ineuron are: {}, {} and {}".format(self.batch1, self.batch2, self.batch3, self.batch4))
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))

# imported package is inherited here as single inheritance
class ineuron_hackthon_companies(ineuron_live_class_batches):
    lp.info("Class is invoked")
    try:
        def __init__(self, company1, company2, company3, company4):
            self.company1 = company1
            self.company2 = company2
            self.company3 = company3
            self.company4 = company4
            lp.info("input values added")
        def hackthon_companies(self):
            print("The hackthon companies in ineuron are: {}, {} and {}".format(self.company1, self.company2, self.company3, self.company4))
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))

class ineuron_partnered_institutions:
    lp.info("Class is invoked")
    try:
        def __init__(self, institution1, institution2, institution3, institution4):
            self.institution1 = institution1
            self.institution2 = institution2
            self.institution3 = institution3
            self.institution4 = institution4
            lp.info("Input values added")
        def institutions(self):
            print("The partnered institution of ineuron are: {}, {} and {}".format(self.institution1, self.institution2, self.institution3, self.institution4))
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))

# mutiple inheritance
class ineuron_employees(ineuron_products, ineuron_hackthon_companies, ineuron_partnered_institutions):
    lp.info("Class is invoked")
    try:
        def __init__(self, employee1, employee2, employee3, employee4):
            self.employee1 = employee1
            self.employee2 = employee2
            self.employee3 = employee3
            self.employee4 = employee4
            lp.info("Input values added")
        def employees(self):
            print("The tech employees of ineuron are: {}, {} and {}".format(self.employee1, self.employee2, self.employee3, self.employee4))
            lp.info("Function execution success")
        def No_of_employees(self,a):
            return "The number of employees in ineuron is {}".format(a)
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))




## Objects to call the classes

try:
    t1 = ineuron_courses("Data science", "Machine Learning", "statistics")
    t2 = one_neuron("Data science", "Machine Learning", "statistics")
    t3 = ineuron_affiliates_market_courses("Data science", "Machine Learning", "statistics")
    t4 = ineuron_products("affiliate marketing", "internship portal", "resume builder", "Paymentr")
    t5 = ineuron_live_class_batches("FSDS Bootcamp 2022", "Data Analytics", "Full stack developer", "Big data bootcamp")
    t6 = ineuron_hackthon_companies("nvidia","redis","Youtube","Geekyants")
    t7 = ineuron_partnered_institutions("Taxila","VIT","KIET","GIM")
    t8 = ineuron_employees("Sagar", "Sunny", "avnish", "manjunath")
    t9 = ineuron_internship_projects("Restaurant Rating Prediction","Basket macth","credit risk analysis","Automatic car parking system")
    t10 = ineuron_jobs("freshworks","Boeing","Greendeck","informatica")
except Exception as e:
    lp.error(e)
    print(str(e))

## polymorphism:
def poly(a):
    try:
        a.courses()
    except Exception as e:
        lp.error(e)
        print(str(e))

poly(t1)
poly(t2)

## Data abstraction(public, private and protected) -- accessing the private variable
try:
    print(t1.course1) # public
    print(t1._course2) # protected
    print(t1._ineuron_courses__course3)  # private

    print(t3.course1) # public
    print(t3._course2) # protected
    print(t3._ineuron_affiliates_market_courses__course3)  # private

    t3._ineuron_affiliates_market_courses__courses()  ## accessing the private function from the class
except Exception as e:
    lp.error(e)
    print(str(e))

## Data encapsulation(Modifying the private varible)
try:
    print(t1._ineuron_courses__course3)
    t1._ineuron_courses__course3 = "Big data"
    print(t1._ineuron_courses__course3)
    t1.courses()

    t1.modify("Big query table")
    print(t1._ineuron_courses__course3)
    t1.courses()
except Exception as e:
    lp.error(e)
    print(str(e))

## Inheritance:
try:
    t1.courses()
    t2.courses()
    t3._ineuron_affiliates_market_courses__courses()
    t3.No_of_courses(121)
    t4.products()
    t5.batches()
    t6.hackthon_companies()
    t7.institutions()
    t8.employees()
    t8.No_of_employees(250)
    t9.ineuron_projects()
    t10.hackthon_jobs()
except Exception as e:
    lp.error(e)
    print(str(e))