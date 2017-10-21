from MyList import MyList
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SliceMaker(object):
  def __getitem__(self, item):
    return item
  def __str__(self):
      return "lol"

s = SliceMaker()

rand = 10

mylist = MyList()
list = []
DEBUG = 1
m_text = "MyList: "
l_text = "List:   "
f = " ---> "

def append(x):
    mylist.append(x)
    list.append(x)
    if DEBUG:
        print("Append " + str(x) + "\n" + l_text + str(list))
        print(m_text + str(mylist))

def stampa():
    print("Stampa\n" + l_text + str(list))
    print(m_text + str(mylist)+"")

def result(m, l):
    if m._compare(l):
        print(bcolors.OKGREEN + "\tSuccess" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Error: " + l_text + " " + str(l) + bcolors.ENDC)
        print(bcolors.FAIL + "Error: " + m_text + " " + str(m) + bcolors.ENDC)

def get_item(x):
    print("get_item[" + str(x) + "]")
    try:
        l = list[x]
        m = mylist[x]
        if DEBUG:
            print(l_text + str(list) + f + str(l))
            print(m_text + str(mylist) + f + str(m))

        result(m, l)

    except IndexError:
        print(l_text + "Errore Indice: " + str(x)) if isinstance(x, int) else print(x)
        print(m_text + "Errore Indice: " + str(x)) if isinstance(x, int) else print(x)

def del_item(x):
    del list[x]
    del mylist[x]
    print("DELETE " + str(x))
    print(l_text + str(list))
    print(m_text + str(mylist))


def set_item(index, l, m):
    list[index] = l
    mylist[index] = m
    print("SET["+str(index)+"], " + str(l) +" " +str(m))
    print(l_text + str(list))
    print(m_text + str(mylist))

    result(mylist, list)





append(4)
append(48)
append(6)
append(5)
append(56)
append(-43)
append(545)
append("e")

print("\n")

list1 = [3,6,4,7]
mylist1 = MyList()
mylist1.append(3)
mylist1.append(6)
mylist1.append(4)
mylist1.append(7)
set_item(s[1:4:1],list1,mylist1)




"""
#get_item(4)
stampa()
get_item(s[1:3:1])
get_item(s[-3:3:2])
get_item(s[-1:-6:-3])
get_item(s[0:3:6])
get_item(s[-1:3:1])
get_item(s[-1:-3:-1])
get_item(s[12:3:])
get_item(s[:3:1])
get_item(s[:3:-1])
get_item(s[1::-2])
get_item(s[-0:-23:-1])
get_item(s[2:2:1])"""

"""for i in range(1000):
    start = randint(-rand,rand)
    stop = randint(-rand,rand)
    step = randint(-rand,rand)
    while step == 0:
        step = randint(-rand, rand)
    get_item(s[start:stop:step])"""




"""
normalList = [3, 5, 8, 1, "casa", 22, 0]

print(lista)
print(normalList)
print(normalList[5::-1])
print(lista[5::-1])

print(mylist"""