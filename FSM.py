import random

node_1 = ['c', 'n']
node_2 = ['s', 'b']
node_3 = ['x', 't']




def choice(node):
    choice = random.choice(node)
    return choice



def generate_string():
    FSM_string = []
    
    N1 = choice(node_1)
    
    FSM_string.append(N1)
    
    if N1 == 'c':
        N2 = choice(node_2)
        if N2 == 'b':
            FSM_string.append(N2)
        elif N2 == 's':
            FSM_string.append(N2)
            while N2 == 's':
                N2 = choice(node_2)
                FSM_string.append(N2)
        
            
    if N1 == 'n':
        N3 = choice(node_3)
        if N3 == 'x':
            FSM_string.append(N3)
        elif N3 == 't':
            FSM_string.append(N3)
    
    return FSM_string

    
            
    
def strings(number):
    for i in range(number):
        print(generate_string())
        
        
        
strings(10)
    
    
   
