#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Simple program for Check if the given point lies inside or outside a polygon?

#program for calculating area of traingle
def aTriangle(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

#for checking on point is inside triangle a triangle or not if sum of
#all triangle formed by point p is equal to original triangle then it lies in that triangle
def inTriangle(a, b, c, i):
    a1 = aTriangle(i[0], i[1], b[0], b[1], c[0], c[1])
    a2 = aTriangle(a[0], a[1], i[0], i[1], c[0], c[1])
    a3 = aTriangle(a[0], a[1], b[0], b[1], i[0], i[1])
    a  = aTriangle(a[0], a[1], b[0], b[1], c[0], c[1])
    return 1 if(a == a1+a2+a3) else 0



poly =  [[0,0], [10, 0], [10, 10], [0, 10]]  #@param 
i = [-1, 10] #@param
total = 0
#now let's consider all the triangle formed by polygon by a fixeted point 'a' in polygon a,  b, c, d...
#plese note that we have not considered in this program but, we must have three or more than three points
#as inpdut to polygon

for m in range(len(poly) - 2):
    total += inTriangle(poly[0], poly[m+1], poly[m+2], i)
if total % 2 ==0:
    print('False')
else:
    print('True')

