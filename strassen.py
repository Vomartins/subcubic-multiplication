#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:11:01 2023

@author: asaa
"""

import sympy as sp

a11 = sp.Symbol('a11')
a21 = sp.Symbol('a21')
a12 = sp.Symbol('a12')
a22 = sp.Symbol('a22')

A = sp.Matrix([[a11,a12], [a21,a22]])

b11 = sp.Symbol('b11')
b21 = sp.Symbol('b21')
b12 = sp.Symbol('b12')
b22 = sp.Symbol('b22')

B = sp.Matrix([[b11,b12], [b21,b22]])

p1 = a21 + a22
p2 = p1 - a11
p3 = a11 - a21
p4 = a12 - p2

q1 = b12 - b11
q2 = b22 - q1
q3 = b22 - b12
q4 = b21 - q2

m1 = a11*b11
m2 = a12*b21
m3 = p1*q1
m4 = p2*q2
m5 = p3*q3
m6 = p4*b22
m7 = a22*q4

r1 = m1 + m4
r2 = r1 + m5
r3 = r1 + m3

c11 = m1 + m2
c21 = r2 + m7
c12 = r3 + m6
c22 = r2 + m3

C = sp.Matrix([[c11,c12], [c21,c22]])

print(sp.simplify(A*B - C))

