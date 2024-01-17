randlist1=[]
randlist2=[]

M = 100
A = 2
C = 1

def linear_random(lenght, seed, randlist1):
    randlist1.append(seed)
    for i in range(lenght):
        randlist1.append((A*randlist1[i] + C) % M)
    print(randlist1)

lenght = int(input('Insert lenght: '))
seed = int(input('Insert seed: '))
linear_random(lenght, seed, randlist1)
linear_random(lenght, randlist1[2], randlist2)