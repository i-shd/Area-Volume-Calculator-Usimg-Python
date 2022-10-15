from tkinter import *
from tkinter import ttk
import sys
import math
pi=math.pi
root = Tk()

# Option Box

var = StringVar(root)
var.set("Functions")


lbl_title = Label(root, text = "WELCOME TO GEOMETRIC SHAPE'S AREA AND VOLUME")
lbl_title.grid(row = 0, column = 0, columnspan = 2, padx =5, pady = 10)

lbl_choose = Label(root, text = "Choose a function, press OK, and go back to IDLE Shell window:")
lbl_choose.grid(row = 1, column = 0, padx = 5, pady = 0, sticky = W)

box = ttk.OptionMenu(root, var, "Area of Triangle", "Area of Circle","Area of Square","Area of Rectangle", "Area of Parallelogram","Volume of Cube","Volume of Cuboid","Volume of Cone","Volume of Sphere","Volume of Hemisphere","Volume of Cylinder")
box.grid(row = 2, column = 0, padx=5, pady=5, sticky= W)

# Separator

line1 = ttk.Separator(root, orient = HORIZONTAL)
line1.grid(row = 4, column = 0, columnspan = 3, sticky = EW) 

# Functions

def area_triangle(a,b,c):
    s=(a + b + c) / 2
    area_tri= (s*(s-a)*(s-b)*(s-c))**0.5
    print("\nThe Area of the Triangle is: " + str(area_tri) + " squared units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")

def area_circle(r):
    area_cir=pi*r*r
    print("\nThe Area of the Circle is: " +str(area_cir)+" squared units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")

def area_sq(l):
    area_s=l**2
    print("\nThe Area of the Square is: " +str(area_s) + " squared units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def area_rect(l,b):
    area_rec=l*b
    print("\nThe Area of the Rectangle is: " +str(area_rec)+" squared units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def area_para(b,h):
    area_parll=b*h
    print("\nThe Area of the Parallelogram is: " +str(area_parll)+" squared units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def vol_cube(l):
    vol_cb=l**3
    print("\nThe Volume of the Cube is: " +str(vol_cb)+" cubed units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def vol_cuboid(l,b,h):
    vol_cbid=l*b*h
    print("\nThe Volume of the Cuboid is: " +str(vol_cbid)+" cubed units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def vol_cone(r,h):
    vol_cn=(1/3)*pi*((r**2)*h)
    print("\nThe Volume of the Cone is: " +str(vol_cn)+" cubed units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def vol_sphe(r):
    vol_sp=(4/3)*pi*(r**3)
    print("\nThe Volume of the Sphere is: " +str(vol_sp)+" cubed units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def vol_hsphe(r):
    vol_hsp=(2/3)*pi*(r**3)
    print("\nThe Volume of the Hemisphere is: " +str(vol_hsp)+" cubed units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
def vol_cyli(r,h):
    vol_cyl=pi*((r**2)*h)
    print("\nThe Volume of the Hemisphere is: " +str(vol_cyl)+" cubed units.")
    print("\nTHANK YOU FOR USING AREA-VOLUME CALCULATOR. HAVE A NICE DAY")
    
# Main Function

def main():
    if var.get() == "Area of Triangle":
        print("You choose Area of Triangle")
        a = float(input("Enter First Side of the Triangle: "))
        b = float(input("Enter Second Side of the Triangle: "))
        c = float(input("Enter Third Side of the Triangle: "))
        area_triangle(a,b,c)
        
    elif var.get() == "Area of Circle":
        print("You choose Area of Circle")
        r = float(input("Enter the Radius of the Circle: "))
        area_circle(r)

    elif var.get() == "Area of Square":
        print("You choose Area of Square")
        l = float(input("Enter the Length of Square: "))
        area_sq(l)

    elif var.get() == "Area of Rectangle":
        print("You choose Area of Rectangle")
        l=float(input("Enter the Length of Rectangle: "))
        b=float(input("Enter the Breadth of Rectangle: "))
        area_rect(l,b)

    elif var.get() == "Area of Parallelogram":
        print("You choose Area of Parallelogram")
        b=float(input("Enter the Base of Parallelogram: "))
        h=float(input("Enter the Height of Parallelogram: "))
        area_para(b,h)

    elif var.get() == "Volume of Cube":
        print("You choose Volume of Cube")
        l=float(input("Enter the Length of Cube: "))
        vol_cube(l)

    elif var.get() == "Volume of Cuboid":
        print("You choose Volume of Cuboid")
        l=float(input("Enter the Length of Cuboid: "))
        b=float(input("Enter the Breadth of Cuboid: "))
        h=float(input("Enter the Height of Cuboid: "))
        vol_cuboid(l,b,h)

    elif var.get() == "Volume of Cone":
        print("You choose Volume of Cone")
        r=float(input("Enter the Radius of Cone: "))
        h=float(input("Enter the Height of Cone: "))
        vol_cone(r,h)

    elif var.get() == "Volume of Sphere":
        print("You choose Volume of Sphere")
        r=float(input("Enter the Radius of Sphere: "))
        vol_sphe(r)

    elif var.get() == "Volume of Hemisphere":
        print("You choose Volume of Hemmisphere")
        r=float(input("Enter the Radius of Hemisphere: "))
        vol_hsphe(r)

    elif var.get() == "Volume of Cylinder":
        print("You choose Volume of Cylinder")
        r=float(input("Enter the Radius of Cylinder: "))
        h=float(input("Enter the Height of Cylinder: "))
        vol_cyli(r,h)

def q():
    sys.exit()

# Function Button
butt1 = ttk.Button(root, text = "OK", command = main)
butt1.grid(row = 2, column = 1, padx = 5, sticky = W)

# Exit Button
butt2 = ttk.Button(root, text = "QUIT", command =q)
butt2.grid(row = 6, column = 0, padx = 5, pady = 5,  sticky = W)

root.mainloop()
    
