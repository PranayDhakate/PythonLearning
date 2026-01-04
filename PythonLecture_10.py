def grt():
    print("Good Morning!")

grt()

def grt_name(name):
    print(f"Good Morning {name}!")
    
grt_name("Sejal")

'''
Print : Only prints the value 
Return : Return the value from the function so we can store it wherever we want
'''

def sqrt(x):
    return x*x
print(sqrt(2))

#Lambda Functn
sqt = lambda x: x*x
sqt(3)

list1 = [1,2,4,6,6,9,7]
sqrts = list(map(lambda x: x*x, list1))
print(sqrts)

even = list(filter(lambda x: x%2 == 0, list1))
print(even)