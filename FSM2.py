import random


# options available at each node
node_1 = ['n', 'c']
node_2 = ['s', 'c']
node_3 = ['x', 'H']
node_4 = ['s', 'v']
node_5 = ['v', 'n']


# number of grammatical strings to return
number = 3

# maximum length of those strings
length = 6


# initialise a string
FSM = []


def N1():
    n1 = random.choice(node_1)
    if n1 == 'n':
        FSM.append(n1)
        N2()
    if n1 == 'c':
        FSM.append(n1)
        N3()


def N2():
    n2 = random.choice(node_2)
    if n2 == 'c':
        FSM.append(n2)
        N4()
    if n2 == 's':
        while n2 == 's':
            FSM.append(n2)
            n2 = random.choice(node_2)
            if n2 == 'c':
                FSM.append(n2)
                N4()
    
    

def N3():
    n3 = random.choice(node_3)
    if n3 == 'x':
        FSM.append(n3)
        N2()
    if n3 == 'H':
        FSM.append('x')
        N5()


def N4():
    n4 = random.choice(node_4)
    if n4 == 'v':
        FSM.append(n4)
        N3()
    if n4 == 's':
        FSM.append(n4)
      
    

def N5(): 
    n5 = random.choice(node_5)
    if n5 == 'n':
        FSM.append(n5)
    if n5 == 'v':
        while n5 == 'v':
            FSM.append(n5)
            n5 = random.choice(node_5)
            if n5 == 'n':
                FSM.append(n5)
    


def runRig():
    N1()
    return FSM

#print(runRig())




def repeatRig(number, length):
    for i in range(number):
        fsm = runRig()
        if len(fsm) > length:
            fsm = fsm[:length-1]
        print(fsm)
        global FSM
        FSM = []

    
repeatRig(number, length)
    
    
    
    


