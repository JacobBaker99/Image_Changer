#Successfully completed Part 1 of the project.
#Also, successfully completed Part 2 of the project.
#Also, successfully completed Part 3 of the project.
import cImage as image
import random
"""Loads specified image filename and does some image processing on it. Displays the original image and then the processed image."""

def load_and_process_image(filename):
    img = image.Image(filename)
    #input for user to choose color
    the_color=input("How would you like " + filename + " processed: random, simon, negative, blackwhite, or wash it in red, green, blue, yellow, magenta, or cyan?")
    the_color= the_color.lower()        
    y=img.getHeight()
    x=img.getWidth()
    window = image.ImageWin( filename, x, y)
    img.draw(window)
    if the_color== ("simon"):
        red_image= sgf(img, x, y, filename)
    elif the_color=="negative":
        red_image = create_negative_image(img)
    elif the_color=="blackwhite":
        red_image=black_and_white(img)
    elif the_color=="random":
        red_image=random(img, x, y, filename)
    else:
        red_image = create_washed_image(img, the_color, filename)
    red_image.draw(window)
    window.exitonclick()

""" this changes the pixels into black and white only."""
def black_and_white (the_image):
    #give an image to alter
    new_image = image.EmptyImage(the_image.getWidth(), the_image.getHeight())
    #the if else statments change the color and let the user decide
    for col in range(the_image.getWidth()):
        for row in range(the_image.getHeight()):
            pixel = the_image.getPixel(col, row)            
            bl_or_wh=(pixel.getRed())+(pixel.getGreen())+(pixel.getBlue())   
            if bl_or_wh <= 382:
                new_red=0
                new_green=0
                new_blue= 0
            else:
                new_red=255
                new_green=255
                new_blue= 255
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            new_image.setPixel(col, row, new_pixel)
    return new_image

"""creates a negative image"""
def create_negative_image(the_image):
    """Creates and returns a negative of the_image"""
    """changes the colors to the opposite to which they are"""
    new_image = image.EmptyImage(the_image.getWidth(), the_image.getHeight())
    for col in range(the_image.getWidth()):
        for row in range(the_image.getHeight()):
            pixel = the_image.getPixel(col, row)
            new_red = 255 - pixel.getRed()
            new_green = 255 - pixel.getGreen()
            new_blue = 255 - pixel.getBlue()
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            new_image.setPixel(col, row, new_pixel)
    return new_image

#part 1
"""changes the color of an image choosen"""
def create_washed_image (the_image, color, filename):
    #give an image to alter
    new_image = image.EmptyImage(the_image.getWidth(), the_image.getHeight())
    #the if else statments change the color and let the user decide
    for col in range(the_image.getWidth()):
        for row in range(the_image.getHeight()):
            pixel = the_image.getPixel(col, row)
            if (color=="red"):
                new_red = pixel.getRed()
                new_green =0
                new_blue = 0
            elif(color=="green"):
                new_red= 0
                new_green=pixel.getGreen()
                new_blue= 0
            elif(color=="blue"):
                new_red= 0
                new_green= 0
                new_blue= pixel.getBlue()
            elif (color=="magenta"):
                new_red= pixel.getRed()
                new_green= 0
                new_blue= pixel.getBlue()
            elif (color=="yellow"):
                new_red=pixel.getRed()
                new_green=pixel.getGreen()
                new_blue= 0
            elif (color== "cyan"):
                new_red=0
                new_green=pixel.getGreen()
                new_blue= pixel.getBlue()       
            elif (color== "quit"):
                print("Thank you for playing!")
            else:
                print ("Invalid Color")
                load_and_process_image(filename)
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            new_image.setPixel(col, row, new_pixel)
    return new_image

"""seperates the image into quadrants and colors them into the simon colors"""
def sgf(img, x, y, filename):
    new_image = image.EmptyImage(img.getWidth(), img.getHeight())
    #the if else statments change the color and let the user decide
    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            pixel = img.getPixel(col, row)
            #x=(x)
            #y=(y)
            v_line=(y/2)
            h_line=(x/2) 
            #quad 2
            if (float(row)) < (float(v_line)) and (float(col)) <= (float(h_line)):
                new_red=0
                new_green=pixel.getGreen()
                new_blue=0
            #quad 3
            elif(float(row)) > (float(v_line)) and (float(col)) < (float(h_line)):
                new_red=pixel.getRed()
                new_green=pixel.getGreen()
                new_blue=0
            #quad 1
            elif(float(row)) < (float(v_line)) and (float(col)) > (float(h_line)):
                new_red=pixel.getRed()
                new_green=0
                new_blue=0
            #quad 4
            elif(float(row)) >= (float(v_line)) and (float(col)) > (float(h_line)):
                new_red=0
                new_green=0
                new_blue=pixel.getBlue()
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            new_image.setPixel(col, row, new_pixel)
    return new_image

""" randomly chooses the colors to wash the image in random quads"""
def random(img, x, y, filename):
    import random
    colors=["pr,z,z","z,pg,z","z,z,pb","z,pg,pb","pr,z,pb","pr,pg,z"]
    color1=random.choice(colors)
    color2=random.choice(colors)
    color3=random.choice(colors)
    color4=random.choice(colors)
    new_image = image.EmptyImage(img.getWidth(), img.getHeight())
    #the if else statments change the color and let the user decide
    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            pixel = img.getPixel(col, row)
            v_line=(y/2)
            h_line=(x/2)
            
            #quad 2
            #j, k, l=color1.split(',')
            if (float(row)) < (float(v_line)) and (float(col)) <= (float(h_line)):
                j, k, l=color1.split(',')
                if j == "pr":
                    new_red=pixel.getRed()
                else:
                    new_red=0
                if k == "pg":
                    new_green=pixel.getGreen()
                else:
                    new_green=0
                if l ==  "pb":
                    new_blue=pixel.getBlue()
                else:
                    new_blue=0
                    
            #quad 3
            elif(float(row)) > (float(v_line)) and (float(col)) < (float(h_line)):
                j, k, l=color2.split(',')
                if j == "pr":
                    new_red=pixel.getRed()
                else:
                    new_red=0
                if k == "pg":
                    new_green=pixel.getGreen()
                else:
                    new_green=0
                if l ==  "pb":
                    new_blue=pixel.getBlue()
                else:
                    new_blue=0

            #quad 1
            elif(float(row)) < (float(v_line)) and (float(col)) > (float(h_line)):
                j, k, l=color3.split(',')
                if j == "pr":
                    new_red=pixel.getRed()
                else:
                    new_red=0
                if k == "pg":
                    new_green=pixel.getGreen()
                else:
                    new_green=0
                if l ==  "pb":
                    new_blue=pixel.getBlue()
                else:
                    new_blue=0

            #quad 4
            elif(float(row)) >= (float(v_line)) and (float(col)) > (float(h_line)):
                j, k, l=color4.split(',')
                if j == "pr":
                    new_red=pixel.getRed()
                else:
                    new_red=0
                if k == "pg":
                    new_green=pixel.getGreen()
                else:
                    new_green=0
                if l ==  "pb":
                    new_blue=pixel.getBlue()
                else:
                    new_blue=0

            new_pixel = image.Pixel(new_red, new_green, new_blue)
            new_image.setPixel(col, row, new_pixel)
    return new_image

"""the beginning"""
"""Entry point of the application."""
def main():
    print("Project 2 by Jacob Baker")
    #input for image to be choosen by user
    stuff=True
    while stuff:
        new_picture=input("What image file would you like to process (It must be a gif.)?")
        
        if new_picture != "quit":
            load_and_process_image(new_picture)
        else:
            print("Thank you for playing!")
            stuff=False
main()
