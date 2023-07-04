#n=int(input())
#for i in range(1,n+1):
#    for j in range(i,i*n+1):
#        print(j,end=" ")
#    print()

import math
pi = math.pi

# Function to take the length of the radius and height of the cone
def cone(r, h):

    # Calculating the surface area
    l = math.sqrt(r * r + h * h)
    SA = pi * r * (r + l)

    # Calculating the volume
    volume = (1 / 3) * pi * r * r * h

    # Printing the surface area and volume
    print("\nSurface Area of Cone = %.2f" % SA)
    print("Volume of Cone = %.2f" % volume)


# Driver code
r = float(input("\nEnter the radius of cone : "))
h = float(input("Enter the height of cone : "))
cone(r, h)