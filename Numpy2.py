from numpy import * 
# simple array using array function from numpy

# a = [[1,9,6],[2,7,5],[5,3,1]]
# b = array(a)
# print(b)

# use range methode 
a = array([range(i,i+3) for i in [2,4,6]])
print(a)

# array contain tuples
b = array([("x",1,True),("y",2,False),("z",3,True)])
print(b)

# empty function   for ceating an  empty matrice 2*3 dimensions
c = empty((2,3))
print(c)

#Random numbers with random (numpy)
 
d = random.uniform(1,40)  # i need one random number in this interval
e = random.uniform(1,40,10) # i need 10 random numbers in this interval
print(d)
print(e)

#Random matrice 0 --1 
f = random.random((2,3))
print(f)

#normal distribution
g = random.normal(0,1,10)
print(g)

#rand int 
h = random.randint(150)
h2 = random.randint(10,size=3)
h3 = random.randint(10,30,size=3)
h4 = random.randint(1,10,(3,3)) #random matrice contain numbers between 1 and 9 
h5 = random.randint(1,10,(3,4,5)) #random matrice with 3 dimensions
h6 = random.randint(1,10,9)
h7 = reshape(h6,(3,3))
print(h7)