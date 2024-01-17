randlist=[]

M = 2147483647
A = 214013
C = 2531011

def linear_random(lenght, seed, randlist):
    randlist.append(seed)
    for i in range(lenght):
        randlist.append((A*randlist[i] + C) % M)
    print(randlist)

lenght = int(input('Insert lenght: '))
seed = int(input('Insert seed: '))
linear_random(lenght, seed, randlist)