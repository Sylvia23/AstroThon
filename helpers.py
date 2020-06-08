#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:16:34 2020

@author: manavmehta
"""

import math

def sin(x): return round(math.sin(math.radians(x)),5)
def cos(x): return round(math.cos(math.radians(x)),5)

def star_distace(star1, star2): # star i: [r, theta, phi]
    r1,t1,p1 = star1[0],star1[1],star1[2]
    r2,t2,p2 = star2[0],star2[1],star2[2]
    ans = 2*r1*r2*(     (sin(t1)*sin(t2)*cos(p1-p2))  +   (cos(t1)*cos(t2))     )
    ans = math.sqrt((r1**2)+(r2**2) - ans)
    return ans

