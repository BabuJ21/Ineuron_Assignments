import logging as lp
class list_tuples_set_dict():
    lp.basicConfig(filename='list_tuples_set_dict12.log', level=lp.INFO, format='%(levelname)s %(asctime)s %(message)s')
    lp.info("Entered into class")
    try:
        def __init__(self,s):
            self.s = s
            lp.info("The input value is declared in the function" + str(self.s))

        def list_extract(self):
            """to extract all the list entity"""
            try:
                for i in self.s:
                    if (type(i) == list):
                        print(i)
                lp.info("List extracted successfully")
            except Exception as e:
                print(e)
                lp.error(e)
        def dict_extract(self):
            """to extract all the dict entity"""
            try:
                for i in self.s:
                    if (type(i) == dict):
                        print(i)
                lp.info("Dictionary extracted successfully")
            except Exception as e:
                print(e)
                lp.error(e)
        def tuples_extract(self):
            """to extract all the tuples entity"""
            try:
                for i in self.s:
                    if (type(i) == tuple):
                        print(i)
                lp.info("tuples extracted successfully")
            except Exception as e:
                print(e)
                lp.error(e)
        def dict_key_values_numeric(self):
            """to extract all the Numeric data it may be a part of dict key and values."""
            try:
                for i in self.s:
                    if type(i) == dict:
                        for j in i.keys():
                            if type(j) == int:
                                print(j)
                        for j in i.values():
                            if type(j) == int:
                                print(j)
                lp.info("Numeric dict data extracted successfully")
            except Exception as e:
                print(e)
                lp.error(e)
        def summation_numeric_data(self):
            """to give summation of all the numeric data."""
            try:
                count = 0
                for i in self.s:
                    if type(i) == (list):
                        for j in i:
                            if type(j) == int:
                                count = count + j
                    if type(i) == tuple:
                        for j in i:
                            if type(j) == int:
                                count = count + j
                    if type(i) == dict:
                        for j in i.values():
                            if type(j) == int:
                                count = count + j
                    if type(i) == dict:
                        for j in i.keys():
                            if type(j) == int:
                                count = count + j
                    if type(i) == set:
                        for j in i:
                            if type(j) == int:
                                count = count + j
                print(count)
                lp.info("summation of all Numeric data is " + str(count))
                lp.info("summation function completed")
            except Exception as e:
                print(e)
                lp.error(e)
        def list_odd_values(self):
            """ to filter out all the odd values out all numeric data which is a part of a list"""
            try:
                for i in self.s:
                    if type(i) == list:
                        for j in i:
                            if type(j) == int:
                                if j % 2 == 1:
                                    print(j)
                                    lp.info("odd values are: " + str(j))
                lp.info("list odd values found")
            except Exception as e:
                print(e)
                lp.error(e)

        def occurrence_data(self):
            """to find out a number of occurance of all the data"""
            try:
                for i in self.s:
                    if type(i) == list:
                        j = 0
                        while j < len(i):
                            print("Number of occurance of {} is :".format(i[j]), i.count(i[j]))
                            j = j + 1
                    if type(i) == tuple:
                        j = 0
                        while j < len(i):
                            print("Number of occurance of {} is :".format(i[j]), i.count(i[j]))
                            j = j + 1
                    if type(i) == set:
                        i = list(i)
                        j = 0
                        while j < len(i):
                            print("Number of occurance of {} is :".format(i[j]), i.count(i[j]))
                            j = j + 1
                    if type(i) == dict:
                        j = 0
                        m = list(i.keys())
                        while j < len(m):
                            print("Number of occurance of {} is :".format(m[j]), m.count(m[j]))
                            j = j + 1
                    if type(i) == dict:
                        k = 0
                        n = list(i.values())
                        while k < len(n):
                            print("Number of occurance of {} is :".format(n[k]), n.count(n[k]))
                            k = k + 1
                lp.info("Occurrences of data function completed")
            except Exception as e:
                print(e)
                lp.error(e)
        def no_of_keys_dict(self):
            """to find out a number of keys in dict element"""
            try:
                for i in self.s:
                    if type(i) == dict:
                        m = list(i.keys())
                        print(len(m))
                        lp.info("No.of keys in dict element is: " + str(len(m)))
                lp.info("Function completed")
            except Exception as e:
                print(e)
                lp.error(e)
        def string_data(self):
            """to filter out all the string data"""
            try:
                for i in self.s:
                    if type(i) == (list):
                        for j in i:
                            if type(j) == str:
                                print(j)
                    if type(i) == tuple:
                        for j in i:
                            if type(j) == str:
                                print(j)
                    if type(i) == dict:
                        for j in i.values():
                            if type(j) == str:
                                print(j)
                    if type(i) == dict:
                        for j in i.keys():
                            if type(j) == str:
                                print(j)
                    if type(i) == set:
                        for j in i:
                            if type(j) == str:
                                print(j)
                lp.info("Funcction completed")
            except Exception as e:
                print(e)
                lp.info(e)
        def alphanum(self):
            """to find out alphanum in data"""
            try:
                for i in self.s:
                    if type(i) == (list):
                        for j in i:
                            if type(j) == str:
                                print(j.isalnum())
                    if type(i) == tuple:
                        for j in i:
                            if type(j) == str:
                                print(j.isalnum())
                    if type(i) == dict:
                        for j in i.values():
                            if type(j) == str:
                                print(j.isalnum())
                    if type(i) == dict:
                        for j in i.keys():
                            if type(j) == str:
                                print(j.isalnum())
                    if type(i) == set:
                        for j in i:
                            if type(j) == str:
                                print(j.isalnum())
                lp.info("alphanum function completed")
            except Exception as e:
                print(e)
                lp.info(e)
        def multiply_numeric(self):
            """to find out multiplication of all numeric value in the individual collection inside dataset"""
            try:
                count = 1
                for i in self.s:
                    if type(i) == (list):
                        for j in i:
                            if type(j) == int:
                                count = count * j
                    if type(i) == tuple:
                        for j in i:
                            if type(j) == int:
                                count = count * j
                    if type(i) == dict:
                        for j in i.values():
                            if type(j) == int:
                                count = count * j
                    if type(i) == dict:
                        for j in i.keys():
                            if type(j) == int:
                                count = count * j
                    if type(i) == set:
                        for j in i:
                            if type(j) == int:
                                count = count * j
                print(count)
                lp.info("The multiplication of all numeric value is: " + str(count))
                lp.info("Function completed")
            except Exception as e:
                print(e)
                lp.error(e)
        def unwrap_list(self):
            """to unwrape all the collection inside collection and create a flat list"""
            try:
                z = []
                for i in self.s:
                    if type(i) == (list):
                        for j in i:
                            z.append(j)
                    if type(i) == tuple:
                        for j in i:
                            z.append(j)
                    if type(i) == dict:
                        for j in i.values():
                            z.append(j)
                    if type(i) == dict:
                        for j in i.keys():
                            z.append(j)
                    if type(i) == set:
                        for j in i:
                            z.append(j)
                print(z)
                print("Number of elements:", len(z))
                lp.info("The final list is: " + str(z))
                lp.info("Function completed")
            except Exception as e:
                print(e)
                lp.error(e)
    except Exception as e:
        print(e)
        lp.info(e)

l =[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
a = list_tuples_set_dict(l)
a.list_extract()
a.dict_extract()
a.tuples_extract()
a.dict_key_values_numeric()
a.summation_numeric_data()
a.list_odd_values()
a.occurrence_data()
a.no_of_keys_dict()
a.string_data()
a.alphanum()
a.multiply_numeric()
a.unwrap_list()