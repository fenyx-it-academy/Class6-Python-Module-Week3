# Write a function sphere_volume that calculates and returns the volume of a sphere when given radius r as a parameter.
#def sphere_volume(r):
    #pi = 3.14
    #return print('Volume is: ', (4*pi*r**3)/3)

# Write a function sphere that calls two other functions that calculate the area of a circle sphere_area and volume of a sphere 
# sphere_volume for a given radius r as a parameter. Functions sphere_area and sphere_volume are nested inside the function sphere.
#  Function sphere returns both the area and the volume of the sphere. (Reproduce sphere_volume function inside function sphere.) 
# Make sure to print the results.
def sphere_area(r):
    pi = 3.14
    area = pi*r**2
    return area
def sphere_volume(r):
    pi = 3.14
    volume = 4/3*sphere_area(r)*r
    return volume
print('Volume is : ',sphere_volume(5))
print('Area is :',sphere_area(5))




