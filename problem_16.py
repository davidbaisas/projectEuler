#!/usr/bin/python

# https://projecteuler.net/problem=16

#time module for calculating execution time
import time

def problem_16():
  a = list(str(2**1000))
  a = [int(x) for x in a]
  pds = sum(a)
  return pds
