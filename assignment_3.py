# I. Write a function sphere_volume that calculates and returns the volume of a sphere when given radius r as a parameter.
# II. Then write a main program that calls sphere_volume to print the volume of a sphere with a radius of 3.
# III. Write a function sphere that calls two other functions that calculate the area of a circle sphere_area and
# volume of a sphere sphere_volume for a given radius r as a parameter.
# Functions sphere_area and sphere_volume are nested inside the function sphere.
# Function sphere returns both the area and the volume of the sphere.
# (Reproduce sphere_volume function inside function sphere.) Make sure to print the results.
import math
r=float(input("Please enter a radius: "))

def sphere_area(r):
    
    A=math.pi*(r**2)
    return A
print(sphere_area(r), "m2")


def sphere_volume(r):
    v=(4/3)*r*sphere_area(r)
    return v
print(sphere_volume(r), "cm3")


def sphere(r):
        
        def sphere_volume(r):
            return
        def sphere_area(r):
            return
    
sphere(r)











