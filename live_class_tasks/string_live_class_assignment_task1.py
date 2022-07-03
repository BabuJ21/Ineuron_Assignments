import logging as lp
lp.basicConfig(filename='string.log', level=lp.INFO, format="%(levelname)s %(asctime)s %(message)s")


class string_asd():
    lp.info("Entered into class string")
    try:
        def __init__(self, s):
            self.s = s
            lp.info("The string value is declared in the function" + str(self.s))

        def string_operations(self):
            lp.info("String operations function invoked and started executing")
            print(self.s[1:300:3])
            print(self.s[::-1])
            a = self.s.upper()
            print(a.split())
            print(self.s.lower())
            print(self.s.upper())
            lp.info("string operations completed")

        def string_expandtabs(self, k):
            lp.info("sting expandtabs function invoked")
            try:
                print(k.expandtabs())
                return k.expandtabs()
                lp.info("string expandtabs function completed")
            except Exception as e:
                print(e)
                lp.error(e)

        def string_strip(self):
            a = input("Enter input to do string strip functions")
            try:
                print(a.strip(),a.lstrip(),a.rstrip())
                return a.strip(), a.lstrip(), a.rstrip()
            except Exception as e:
                print("please provide correct string input")
                lp.error(e)

        def string_replace(self):
            lp.info("string replace function invoked and executing")
            d = input("Enter a sentence")
            e = input("Enter the string value from sentence: ")
            f = input("Enter the string value to replace with: ")
            lp.info("The inputs are %s \n %s \n %s", d, e, f)
            try:
                print(d.replace(e,f))
                return d.replace(e, f)
                lp.info("string replaced successfully")
            except Exception as e:
                print(e)
                lp.error(e)

        def string_center(self):
            lp.info("String center function invoked and started")
            d = input("Enter a string word")
            lp.info("The input is %s", d)
            try:
                print(d.center(100,'#'))
                return d.center(100, '#')
                lp.info("string center function completed")
            except Exception as e:
                print(e)
                lp.error(e)
    except:
        print("please provide input for the class")


a = string_asd('this is My First Python programming class and i am learNING python string and its function')
a.string_operations()
a.string_expandtabs('asdf\tpqrs\tis\tmy\tfavourite\tkeyboard\tletters\tfor\ttyping')
a.string_center()
a.string_replace()
a.string_strip()
