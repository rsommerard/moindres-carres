# -*- coding: utf8 -*-

import numpy
from matplotlib import pyplot

def load_data():
  """
    Charge les données des fichiers textes.
  """
  global x, y, N, t, p
  t = numpy.loadtxt('data/t.txt')
  N = len(t)
  x = numpy.vstack((t, numpy.ones(N)))
  p = numpy.loadtxt('data/p.txt')
  y = p

def print_results():
  """
    Affiche les résultats.
  """
  print 'FAA - TP1: Moindres carrés'
  print '-' * 80
  print 'Nombre de données: {0}'.format(N)
  print '-' * 80
  print 'Théta: {0}'.format(theta())
  print '-' * 80
  print 'Erreur quadratique: {0}'.format(j_theta())
  print '-' * 80

def theta():
  """
    Calcul théta par la méthode des moindres carrés pour x et y.
  """
  return numpy.dot(numpy.linalg.inv(numpy.dot(x, x.T)), numpy.dot(x, y))

def f_theta():
  """
    Calcul le y pour les x en fonction de théta.
  """
  return numpy.dot(theta().T, x)

def j_theta():
  """
    Calcul de l'erreur quadratique.
  """
  tmp = (y - numpy.dot(x.T, theta()))
  return ((1.0/N) * numpy.dot(tmp.T, tmp))

def print_graphs():
  """
    Affiche les données sur le graph.
  """
  pyplot.plot(t, p, '.', label='data')
  pyplot.plot(t, f_theta(), label='f(x)')
  pyplot.ylabel('position (m)')
  pyplot.xlabel('temps (s)')
  pyplot.legend()
  pyplot.show()

def main():
  """
    Fonction principale du programme.
  """
  load_data()
  print_results()
  print_graphs()

if __name__ == '__main__':
  main()
