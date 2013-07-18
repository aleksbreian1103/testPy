print('sp\xc4m')
print('spam'.encode('utf8'))
print('spam'.encode('utf16'))
print('sp\xc4\u00c4\U000000c4m')

print('x' + b'y'.decode())
print('x'.encode() +b'y')
# Pattern matching
import re
match = re.match('Hello[ \t]*(.*)world', 
                 'Hello    Python  world')
print(match.group(1))
match = re.match('[/:](.*)[/:](.*)[:](.*)',
                 '/usr/home:lumberjack')
print(match.groups())
M = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(M)
print(M[1])

diag = [ M[i][i] +1 for i in [0, 1 ,2] ]
print(diag)

doubles = ( c*2 for c in 'spam')
print(doubles)
for i in doubles:
    print(i, end = '')
print('\n')    
# Create a generator object    
G = ( sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print(G)
for i in G:
    print(next(G))

# Map: use with list in #3.X
print(list(map(sum, M)))

# Set
print({sum(row) for row in M})

# Dict
print({i : sum(M[i]) for i in range(3)})

print([ ord(x) for x in 'spaam'])

print({ord(x) for x in 'spaam'})

print({x : ord(x) for x in 'spaam'})

test = ( ord(x) for x in 'spaam')
print(test)
for i in test:
    print(i)


print( dict(zip(['name', 'job', 'age'], ['Aleks', 'finance', '28'])))

rec = {'name' : {'first' : 'Aleksander', 'last' : 'Hansen'}, 'job' : ['finance', 'portfolio'], 'age' :'28'}
print(rec)
print(rec['name']['last'])
print(rec['job'][1])
rec['job'].append('risk manager')
print(rec)

rec['job'].pop()
print(rec)

print(rec.get('job', 0))

D = { 'a': 1, 'b': 2, 'c': 3}
print(D)
Ks = list(D.keys())
print(Ks)

Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])
    
# reduce 3-step process to one step:
for key in sorted(D):
    print(key, '=>', D[key])    

y = {x**2 for x in [1, 2, 3, 4]}
print(y)

print({x for x in 'spam'})

print({c*4 for c in 'spam'})

S = {c*4 for c in 'spam'}
print(S)

# Set OR
print( S | {'mmmm', 'xxxx'} )

# Set AND (in both sets)/intersection
print( S & {'mmmm', 'xxxx'})

L = [1, 2, 1, 3, 2, 4, 5]
print(L)
print(set(L))

# Convert back to list after removing duplicates
L = list(set(L))
print(L)

y = list( set( ['yy', 'cc', 'aa', 'xx', 'dd', 'aa'] ) ) 
print(y)
print(sorted(y))

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print (L1 == L2)

print(set(L1) == set(L2))

print( sorted(L1) == sorted(L2) )

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom',  'sue'}

# XOR (are not in both sets)
print(managers ^ engineers)

# Set union
print( (managers|engineers) - (managers^engineers) )

print( True + 1 )
 

# Chapter 9 - Tuples and Files

print((1, 2) + (3, 4))
print( (1, 2) *4 )

T = (1, 2, 3, 4)
print(T[0], T[1:3]) 
print(T[1:3])

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
print(tmp)
T = tuple(tmp)
print(T)
print(sorted(T))

# List comprehensions on tuples:
T = (1, 2, 3, 4, 5)
L = [x+20 for x in T]
print(L)

T = (1,2, 3, 2, 4, 2)
print( T.index(2,2))

print( T.count(2) )

T = (1, [2, 3], 4)
# cannot change tuple itself
#T[1] = 'spam'

# but we can change mutables inside a tuple
T[1][0] = 'spam'
print(T)

# tuple as records
bob = ('Bob', 40.5, ['dev', 'mgr'])
print(bob)

print(bob[0], bob[2])

bob = dict(name = 'Bob', age = 40.5, jobs = ['dev', 'mgr'])
print(bob)
print(bob['name'], bob['jobs'])

#converting to a tuple
print(tuple(bob.values()))
print(tuple(bob.items()))
print(list(bob.items()))

# access tuple by both key and position
from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
print(Rec)
bob = Rec('Bob', age = 40.5, jobs = ['dev', 'mgr'])
print(bob)
# Access by position
print(bob[0], bob[2])
# Access by 'key'/attribute
print(bob.name, bob.jobs)

# Coverting to a dictionary supports key-based behavior when needed:
O = bob._asdict()
print(O)
print(O['name'], O['jobs'])
# Tuple assignment
name, age, jobs = bob
print(name, jobs)
# Iteration context
for x in bob: print(x)

























