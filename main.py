#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as plt

t = np.loadtxt("data/t.txt")
print '-' * 80
print 't = {0}'.format(t)

p = np.loadtxt("data/p.txt")
print '-' * 80
print 'p = {0}'.format(p)

N = len(t)

x = np.vstack((t, np.ones(N)))
print '-' * 80
print 'x = {0}'.format(x)

y = p
print '-' * 80
print 'y = {0}'.format(y)

#print np.dot(x, x.T)

#print np.linalg.inv(np.dot(x, x.T))

#print np.dot(x, y)

O = np.dot(np.linalg.inv(np.dot(x, x.T)), np.dot(x, y))
print '-' * 80
print 'O = {0}'.format(O)

fO = np.dot(O.T, x)
print '-' * 80
print 'fO = {0}'.format(fO)

A = (y - np.dot(x.T, O))

JO = ((1.0/N) * np.dot(A.T, A))
print '-' * 80
print 'JO = {0}'.format(JO)

print '-' * 80

plt.plot(t, p, '.')
plt.plot(t, fO)
plt.ylabel('position (m)')
plt.xlabel('temps (s)')
plt.show()
