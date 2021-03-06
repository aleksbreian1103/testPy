#print('sp\xc4m')
print('spam'.encode('utf8'))
print('spam'.encode('utf16'))
#print('sp\xc4\u00c4\U000000c4m')

print('x' + b'y'.decode())
print('x'.encode() +b'y')
# Pattern matching
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
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
    print(i)
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
print('\n')
bob = {'name': 'Bob', 'age':40.5, 'jobs': ['dev', 'mgr']}
job, name, age = bob.values()
print(name, job)
print('\n')
for x in bob: 
    print(bob[x])

for x in bob.values():
    print(x)

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a':1, 'b':2}
L = [1, 2, 3]

print(X, Y, Z)
print(S)
print(D)
print(L)

print('')

F = open('datafile.txt', 'w')
print( F.write(S + '\n') )
print( F.write('%s, %s, %s\n' % (X, Y, Z) ) )
print( F.write( str(L) + '$' + str(D) + '\n') )
F.close()

chars = open('datafile.txt', 'r').read()
print(chars)

F = open('datafile.txt', 'r')
line = F.readline()
print(line)
print(line.rstrip())

line = F.readline()
print(line)

parts = line.split(',')
print(parts)
#print( line.strip('4'))
print( int(parts[1]) )

numbers = [ int(p) for p in parts ]
print(numbers)

line = F.readline()
print(line)
parts = line.split('$')
print(parts)

objecto = [ eval(p) for p in parts ]
print(objecto)

print('')
# Storing Native Python Objects: pickle

D = {'a' : 1, 'b' : 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)

print('')
# JSON

name = dict(first = 'Bob', last = 'Smith')
rec = dict( name = name, job = ['dev', 'mgr'], age = 40.5)
print(rec)
print(rec['name']['first'])

print('')

import json
print(json.dumps(rec))

S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)

print(O == rec)
print('')

json.dump(rec, fp = open('testjson.txt', 'w'), indent = 4)
print( open('testjson.txt').read() )

P = json.load(open('testjson.txt'))
print(P)

print('')

# Storing binary data: the C struct
F = open('data.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)
values = struct.unpack('>i4sh', data)
print(values)

print('')

# File context managers
#with open(r'/Users/Aleks/data.txt') as myfile:
#    for line in myfile:
#        print(line)

# Object Flexibility: nested compound sequence objects:
L = [ 'abc', [ (1, 2), ([3], 4)], 5]
print(L)
print(L[1][1])
print(L[1][1][0])
print(L[1][1][0][0])
print(L[1][0][1])

2**16
65536
2/5, 2/5.0
(0, 0.4)
3/5

'spam' + 'eggs'

S = 'ham'
'eggs' + S
S*5
S[:0]
S[:1]
S[0:]

print('green %s and %s' % ('eggs', S))
'green {0} and {1}'.format('eggs', S)

print('x'[0])

print(('x',)[0])

#('x',)[1]

print(('x', 'y')[1])

L = [1, 2, 3] + [4, 5, 6]
print(L)
print(L[:])

print(L[:0])
print(L[-2])

print(L[-2:])

print( ( [1,2,3], [4,5,6] )[2:4] )
print( ( [1,2,3], [4,5,6] )[0:1] )
print( ( [1,2,3], [4,5,6] )[0][2] )
print( [ L[2], L[3] ] )
print( L.reverse() )

print( L.sort() )

print(L.index(4))


print( {'a':1, 'b':2}['b'] )

D = {'x':1, 'y':2, 'z':3}
print(D)
D['w'] = 0
print(D['x']+D['w'])
D[(1,2,3)] = 4
print(list(D.keys()) )
print( D[(1,2,3)] )
print( list(D.items()) )
print( list(D.values()) )
print( (1,2,3) in D )


print( [[]], ['', [], (), {}, None] )

L = [0,1,2,3]
print(L)
#L[4]
print( L[-1000:100] )
print( L[3:1] )
L[3:1] = ['?']
print( L )

L = [0, 1, 2 ,3]
L[2] = []
print(L)

L[2:3] = []
print(L)

del L[0]
print(L)

del L[1:]
print(L)

#L[1:2] = 1

# Section II, Q4: Tuple assignment
X = 'spam'
Y = 'eggs'
print(X, Y)
X, Y = Y, X
print(X, Y)

# Q5: Dictionary keys
D = {}
D[1] = 'a'
D[2] = 'b'  # The keys are not accessed by offsets. However, numbers are immutable, and
# any hashable object kan be used as a key. Also, dictionaries support assignment "out-of-bounds"
print(D)

D[(1, 2, 3)] = 'c'
print(D)
print('')

# Q6: Dictionary indexing
D = {'a' : 1, 'b' : 2, 'c' : 3}
print(D)
#D['d']
D['d'] = 'spam'
print(D)
print('')

#Q8: Generic options
S = 'spam'
print(S[0][0][0][0][0])
S = ['s', 'p', 'a', 'm']
print( S[0][0][0][0][0] )
print('')

# Q9: Immutable types
S = 'spam'
S = S[:1] + 'lam'
print(S)
S = S[0] + 'lam'
print(S)
print('')

# Q10: Nesting
D = {'name': {'first': 'Aleks', 'last': 'Hansen'}, 'age': 28,
      'email': 'aleksbreian@gmail.com', 'phone': 3147073062}
print(D['name']['last'])

print('')

# Q11:
F = open('myfile.txt', 'w')
F.write('Hello file world!\n')
F.write('Wonder if this works\n')
F.close()

F = open('myfile.txt')
print(F.read())
#for line in F:
#    print(line, end = '')
F.close()

print('')


import sys
print(sys.version)

print('')

#while True:
#    reply = input('Enter text:')
#    if reply == 'stop' or 'STOP' or 'Stop': break
#    print(int(reply) ** 2)
#print('Bye')

print(open('script2.py', 'r').read())
#open('script2.py','r').read()
f = open('script2.py', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f = open('script2.py', 'r')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

# Old way, loads entire file into memory
for line in open('script2.py', 'r').readlines():
    print(line.upper(), end='')

print('')

# New better way
for line in open('script2.py', 'r'):
    print( line.upper(), end='')
 
print('\n')
 
# next() f.__next__()
f = open('script2.py', 'r')
print(f.__next__())
print(f.__next__())

print('')

#Easier next() method:
f = open('script2.py', 'r')
print(next(f))
print(next(f))

L = [1, 2, 3]
I = iter(L)
print(I.__next__())
print(I.__next__())
print(I.__next__())
#print(I.__next__() )
print('')

f = open('script2.py', 'r')
print(iter(f) is f)
print(iter(f) is f.__iter__())
print(f.__next__())

print('')

# usual way to get the keys in a dictionary
D = {'a': 1, 'b': 2, 'c': 3}
for key in D.keys():
    print(key, D[key])

print('')

#Dictionaries are iterables with an interator that automatically
# returns one key at a time:
I = iter(D)
print(next(I))
print(next(I))
print(next(I))

print('')
# Don't have to call the keys() method to step through dictionary keys
for key in D:
    print(key, D[key])

R = range(5)
print(R)
for num in R:
    print(num, end='')
print('\n', list(R))

E = enumerate('spam')
print(E)
I = iter(E)
print(next(I))
print(list(enumerate('spam')))

L = [1, 2, 3, 4]
L = [x + 10 for x in L]
print(L)

for line in  open('script2.py', 'r'):
    print(line, end='')

print('')

line = open('script2.py', 'r')
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)

#shorter - don't open the file separately
lines = [line.rstrip() for line in open('script2.py', 'r')]
print(lines)

#uppercase
upper = [line.upper() for line in open('script2.py', 'r')]
print(upper)

upperstripped = [line.upper().rstrip() for line in open('script2.py', 'r')]
print(upperstripped)

replaced = [line.replace(' ', '!').rstrip() for line in open('script2.py', 'r')]
print(replaced)

true_test = [('sys' in line, line[:5]) for line in open('script2.py', 'r')]
print(true_test)

lines = [line.rstrip() for line in open('script2.py', 'r') if line[0] == 'p']
print(lines)

lines = [line.rstrip()[-1:] for line in open('script2.py', 'r') if line.rstrip()[-1:].isdigit()]
print(lines)
lines = [line.rstrip() for line in open('script2.py', 'r') if line.rstrip()[-1:].isdigit()]
print(lines)

length = len(open('script2.py', 'r').readlines())
print(length)

print(len([length for length in open('script2.py', 'r') if length.strip() != '']))

ordered_collection = [x + y for x in 'abc' for y in 'lmn']
print(ordered_collection)

print({i: line.rstrip()
       for (i, line) in enumerate(open('script2.py', 'r')) if line[0] == 'p'})

# Generator expression
lines = (line.upper() for line in open('script2.py', 'r'))
print(lines)
print(list(lines))

# *arg can be in function calls to unpack a collection of
# values into individual arguments.


def f(a, b, c, d):
    print(a, b, c, d, sep='&')

f(1, 2, 3, 4)
f(*[1, 2, 3, 4])
f(*open('script2.py', 'r'))

X = (1, 2)
Y = (3, 4)
print(list(zip(X, Y)))

A, B = zip(*zip(*zip(*zip(X, Y))))
print(A, B)

#print(2**38)
#F = [line for line in open('challenge_two.txt', 'r')]
#F = str(F)


#def trans(char):
#    if ord(char) > ord('z') or ord(char) < ord('a'):
#        return char
#    else:
#        return chr(ord('a') + (ord(char) - ord('a') + 2) % 26)

#print( ''.join(trans(char) for char in F), end = '' )

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y):
    return x < y

def morethan(x, y):
    return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(morethan, 4, 2, 1, 5, 6, 3))

def func(a, *b, c = 6, **d):
    print(a, b, c, d)
    
func(1, *(2, 3), **dict(x = 4, y = 5))
func(1, *(2, 3), c = 7, **dict(x = 4, y = 5))
func(1, c = 7, *(2, 3), **dict(x = 4, y = 5))
func(1, *(2, 3), **dict(x = 4, y = 5, c = 7))


def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res

s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'

print(intersect(s1, s2), union(s1, s2))
print(intersect([1, 2, 3, 4], (1, 4)))
print(intersect(s1, s2, s3))  
print(union(s1, s2, s3))

def tester(func, items, trace = True):
    for i, _ in enumerate(items):
        items = items[1:] + items[:1]
        if trace:
            print(items)
        print(sorted(func(*items)))
        
tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
tester(union, ('a', 'abcdefg', 'abdst', 'albmnc'), False)
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmncd'), False)

"""
Emulate most of the 3.X print function for use in 2.X (and 3.X).
Call signature: print3(*args, sep = ' ', end = '\n', file = sys.stdout)
"""
#import sys

def print3(*args, **kargs):
    sep = kargs.get('sep', ',')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
    
print3(1, 2, 3)
print3(1, 2, 3, sep = '')
print3(1, 2, 3, sep = '...')
print3(1, [2], (3,), sep = '...')

print3(4, 5, 6, sep = '', end = '')
print3(7, 8, 9)
print3()

#print3(1, 2, 3, sep = '??', end = '.\n', file = sys.stderr)

"""
Use 3.X keyword-only args
"""
def print31(*args, sep = ' ', end = '\n', file = sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
    
"""
Use 2.X/3.X keyword ars deletion with defaults
"""
def print32(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

#print32(99, name = 'bob')
print32(4, 5, 6, sep = ',')
    
"""
Advanced Function Topics.
"""
# Recursion
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
print(mysum([1, 2, 3, 4, 5]))

def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])

print(mysum2([1, 2, 3, 4]))

# mysum3 and mysum3 fail for empty lists but allow for sequences
# of any object type that supports +, not just numbers.
def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:])

# mysum4 works for arbitrary iterables, including open input files.
def mysum4(L):
    first, *rest = L
    return first if not rest else first + mysum4(rest)

print(mysum4([1]))
print(mysum4([1, 2, 3, 4, 5]))
print(mysum4(('s', 'p', 'a', 'm')))
print(mysum4(['spam', 'ham', 'eggs']))
print(mysum4(open('script2.py', 'r')))

print('')

def mysum5(L):
    if not L: return 0
    return nonempty(L)
    
def nonempty(L):
    return L[0] + mysum5(L[1:])


print(mysum5([1.1, 2.2, 3.3, 4.4]))

L = [1, 2, 3, 4, 5]
sumone = 0
while L:
    sumone += L[0]
    L = L[1:]
print(sumone)

sumone = 0
L = [1, 2, 3, 4, 5]
for x in L:
    sumone += x
print(sumone)

# Handling arbitrary sructures

L = [1, [2, [3, 4], 5], 6, [7, 8]]

#Sumtree
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

print(sumtree(L))

print('')

# lambda
f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

z = (lambda a = 'fee', b = 'fie', c = 'foe': a + b + c)
print(z('wee'))

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights()
msg = act('robin')
print(msg)

print('')

#lambda works inside a list literal
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))
print(L[1](3))
print(L[-1](3))

print('')

key = 'got'
print({'already': (lambda: 2 + 2),
'got': (lambda: 2 * 4),
'one': (lambda: 2 ** 6)}[key]())

print('')

lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))

showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])
print(t)

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))
print(t)


showall = lambda x: [print(line, end = '') for line in x]
t = showall('linefor all')
print(t)

showall = lambda x: print(*x, sep = '', end = '') 
t = showall('line')
print(t)

print('')

def action(x):
    return (lambda y: x + y)

act = action(99)
print(act(2))

action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))

print(((lambda x: (lambda y: x + y))(99))(4))

#from tkinter import Button, mainloop
#x = Button(
#           text = 'Press me',
#           command = (lambda: sys.stdout.write('Spam\n')))
#x.pack()
#mainloop()
 
# Functional programming tools
          
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)

print(updated)

def inc(x):
    return x + 10

print(list(map(inc, counters)))

print(list(map((lambda x: x + 3), counters)))

def mymap(func, seq):
    res = []
    for x in seq: 
        res.append(func(x))
    return res

print(mymap(inc,counters))

print(list(map(inc, [1, 2, 3])))
print(mymap(inc, [1, 2, 3]))

print('')

print(list(map(pow, [1, 2, 3], [2, 3, 4])))

print(list(map(inc, [1, 2, 3, 4])))
print([inc(x) for x in [1, 2, 3, 4]])

print(list(filter((lambda x: x> 0), range(-5, 5))))

print([x for x in range(-5,5) if x > 0])

from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res += x

print(res)

def myreduce(function, sequence):
    tally = sequence[0]
    for each in sequence[1:]:
        tally = function(tally, each)
    return tally

print(myreduce((lambda x, y: x + y), [1, 2, 3, 4]))

# Generators
## Generator functions
def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i, end = ':')

print('')

x = gensquares(4)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#print(next(x))

# Generator functions return themselves for iter because they support next directly.
y = gensquares(5) #returns a generator wich is its own iterator.
print(y)
print(iter(y) is y)
print(next(y))
print(next(y))

for x in [n ** 2 for n in range(5)]:
    print(x, end = ' : ')

print('')
print([n ** 2 for n in range(5)])

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print(tuple(ups('aaa,bbb,ccc')))

print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})

def gen():
    for i in range(10):
        X = yield i
        print(X)
        
G = gen()
print(G)
print(next(G))
print(G.send(77))
print(G.send(88))
print(next(G))

# List comprehension
print([x ** 2 for x in range(4)])

print((x ** 2 for x in range(4)))
print(list(x ** 2 for x in range(4)))

G = (x ** 2 for x in range(4))
print(iter(G) is G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print('')

for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num/2.0))

print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))

print('')
a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, b, c)

print(sum(x ** 2 for x in range(4)))
print(sorted(x ** 2 for x in range(4)))
print(sorted((x **2 for x in range(4)), reverse=True))

print(list(map(abs, (-1, -2, 3, 4))))
print(list(abs(x) for x in (-1, -2, 3, 4)))

print(list(map(lambda x: x * 2, (1, 2, 3, 4))))
print(list(x *2 for x in (1, 2, 3,4)))

line = 'aaa,bbb,ccc'
print(''.join(x.upper() for x in line.split(',')))
print(''.join(x * 2 for x in line.split(',')))

print('')
print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])
print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))
print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))

import math
print(list(map(math.sqrt, (x ** 2 for x in range(4)))))

import os
for (root, subs, files) in os.walk('.'):
    for name in files:
        if name.startswith('call'):
            print(root, name)
            
def f2(a, b, c):
    print('%s %s and %s' % (a, b, c))

#Normal positionals    
f2(0, 1, 2)
#unpack range values: iterable in 3.X
f2(*range(3))
#unpack generator expreesion values
f2(*(i for i in range(3)))

D = dict(a = 'Bob', b = 'dev', c = 40.5)
print(D)

#Normal keywords
f2(a = 'Bob', b = 'dev', c = 40.5)
# Unpack dict: key = value
f2(**D)
#Unpack keys iterator
f2(*D)
#Unpack view itereator: iterable in 3.X
f2(*D.values())

for x in 'spam':
    print(x.upper(), end = ' ')
    
print('')
list(print(x.upper(), end = ' ') for x in 'spam')
print('')
print(*(x.upper() for x in 'spam'))

# Generating scrambled sequences.



