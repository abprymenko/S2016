import requests
import inspect as ins

#help(requests)

students = list()
#for method in dir(students):
#    print(method)
#print(hasattr(students, "__iadd__"))
#print(getattr(students, "copy"))
#print(getattr(students, "append1", None))
'''
print(callable(requests.get))
print(callable(requests.__title__))
r = requests.get('https://www.python.org')
print(r.status_code)
print(r.content)
'''

class CustomException(Exception):
    pass
class CustomTest:
    pass
#print(issubclass(CustomException, Exception))
#print(issubclass(CustomTest, Exception))
#print(issubclass(CustomTest, object))
#print(issubclass(Exception, object))
'''
custExc = CustomException()
cusTest = CustomTest()
print(isinstance(custExc, object))
print(isinstance(custExc, BaseException))
print(isinstance(custExc, Exception))
print(isinstance(custExc, CustomException))
print(isinstance(cusTest, CustomTest))
print(isinstance(cusTest, CustomException))
'''
'''
print(ins.isclass(CustomException))
print(ins.isfunction(requests.get))
print(ins.isfunction(requests.post))
print(ins.isfunction(requests.put))
print(ins.ismethod(requests.patch))
print(ins.ismodule(requests))
print(ins.getmodule(requests))
'''
import  colorama
'''

'''