#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Revised: program to calculate sun covered sun
#Three different techniques using at same 


#program to calculate height and width of rectangular building
def boxdia(a, b, c, d):
    height = b[1] - a[1]
    width = c[0] - b[0]
    return abs(height), abs(width)

#input must be in multiplication of 4 metrix as 4 metrix represent a box
#a special case when height of building is parallel to sun 
def buildings(a, b):
    if (b[1] < a[0][0][1]):
        #If only one building
        if len(a[0]) == 1:
            height, _ = boxdia(a[0][0], a[0][1], a[0][2], a[0][3])
            print(float(height))
        else:
            #for multiple bulding
            heights = []
            widths = []
            for i in range(len(a)):
                height, width = boxdia(a[i][0], a[i][1], a[i][2], a[i][3])
                total_f = height + width
                heights.append(height)
            for i in range(len(a) - 1):
                if a[i] < a[i+1]:
                    new_hei = a[i+1] - a[i]
                    total_n += new_hei
            print(float(total_f + total_n))
    else:
        #when sun is above buiding
        #and there are more than one building
        if len(a) > 1:
            print("to be calculated")
        else:
            #sun is above and only one building
            height, width = boxdia(a[0][0], a[0][1], a[0][2], a[0][3])
            print(float(height + width))

            
#case 1
a = [[[4,0],[4,-5],[7,-5],[7,0]]]
b = [1, 1]
print(buildings(a, b))

#case 2            
a = [[[4,0],[4,-5],[7,-5],[7,0]], [[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]]
b = [-3.5,1]
print(buildings(a,b))


