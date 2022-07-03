import logging as lp
class list_tuples_set_dict():
    lp.basicConfig(filename='list_tuples_set_dict.log', level=lp.INFO, format='%(levelname)s %(asctime)s %(message)s')
    lp.info("Entered into class")
    try:
        def __init__(self,s):
            self.s = s
            lp.info("The input value is declared in the function" + str(self.s))

        def operations(self):
            lp.info("operations function invoked and started executing")
            print("list reverse:" ,self.s[::-1])
            print("Accessing 234 value from list:" ,self.s[7][0])
            print("Accessing 456 value from list:" ,self.s[5][1])
            print("Accessing sudh value from list:", self.s[-1]['key1'])
            lp.info("list basic operations completed")

        def list_extract(self):
            lp.info("list extraction function invoked")
            try:
                k = []
                for i in self.s:
                  if type(i) == list:
                      k.append(i)
                print(k)
                return k
                lp.info("list extraction function completed")
            except Exception as e:
                print(e)
                lp.error(e)

        def dict_keys(self):
            lp.info("Dictionary keys function started")
            try:
                for i in self.s:
                  if type(i) == dict:
                      print(i.keys())
                lp.info("Dictionary keys function completed")
            except Exception as e:
                lp.error(e)

        def dict_values(self):
            lp.info("Dictionary values function started")
            try:
                for i in self.s:
                  if type(i) == dict:
                      print(i.values())
                lp.info("Dictionary values function completed")
            except Exception as e:
                lp.error(e)
    except Exception as e:
        print(e)
        lp.info(e)


k = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh", 234:[23,45,656]}]
a = list_tuples_set_dict(k)
a.dict_keys()
a.dict_values()
a.list_extract()
a.operations()