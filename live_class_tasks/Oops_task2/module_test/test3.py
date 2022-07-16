from Task2.log import *

class ineuron_internship_projects:
    lp.info("Class is invoked")
    try:
        def __init__(self, project1, project2, project3, project4):
            self.project1 = project1
            self.project2 = project2
            self.project3 = project3
            self.project4 = project4
            lp.info("Input values added")
        def ineuron_projects(self):
            print("The internship projects offered by ineuron are: {}, {} and {}".format(self.project1, self.project2, self.project3, self.project4))
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))

# inheritance
class ineuron_jobs(ineuron_internship_projects):
    lp.info("Class is invoked")
    try:
        def __init__(self, job1, job2, job3, job4):
            self.job1 = job1
            self.job2 = job2
            self.job3 = job3
            self.job4 = job4
            lp.info("Input values added")
        def hackthon_jobs(self):
            print("The jobs from ineuron are: {}, {} and {}".format(self.job1, self.job2, self.job3, self.job4))
            lp.info("Function execution success")
    except Exception as e:
        lp.error(e)
        print(str(e))