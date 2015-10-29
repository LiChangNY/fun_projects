"""
Good tutorials
http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

Warning message when running scripts, but shouldn't affect anything.
http://stackoverflow.com/questions/30818222/python-2-7-9-mac-os-10-10-3-message-setcancycle-is-deprecated-please-use-setc
"""

import Tkinter
import turtle
import time

# set attributes
branch = 77
pen = 6

# define colors for trunk/branch and leaves
def select_color(tt, branchLen, divide_one, divide_two, color_one, color_two):
	if branchLen > divide_one:
		tt.color(color_one)
	elif branchLen > divide_two:
		tt.color(color_two)

# functions to draw tress    
def tree(theta_one, theta_two, branchLen, divide_one, divide_two, tt, pen, color_one, color_two):
	
	# set attribute
	tt.pensize(pen)
	
	# base case
	if branchLen < divide_two:
		return
    
    
    # pick colors for drawing
	select_color(tt, branchLen, divide_one, divide_two, color_one, color_two)
	
	# recursion starts from here
	tt.forward(branchLen)
	tt.right(theta_one)
	tree(theta_one, theta_two, branchLen*0.75, divide_one, divide_two, tt, pen * 0.8, color_one, color_two)
	tt.left(theta_one + theta_two)
	tree(theta_one, theta_two, branchLen*0.65, divide_one, divide_two, tt, pen * 0.8, color_one, color_two)
	tt.right(theta_two)

    # call second time to prevent over-coloring
	select_color(tt, branchLen, divide_one, divide_two, color_one, color_two)

	# return to instance
	tt.backward(branchLen)
	turtle.hideturtle()

def main():

    tt = turtle.Turtle()
    
    # set up canvas
    window = turtle.Screen()
    window.bgcolor("#ccffcc")
    window.title("life of a tree") 
    
    # define pointer
    tt.shape('blank')
    tt.speed(0)    

    # define initial point
    tt.left(90)
    tt.up()
    tt.backward(100)
    tt.down()
    
    #************************************************************************************#
    ##### Spring doesn't take that long to draw, so I made it completely animated.########
    ############ Uncomment codes below as instructed to see the full animation ###########
    #************************************************************************************#
    
    # draw trees
    # spring
    tree(30, 60, branch, branch*0.25, branch*0.10, tt, pen, "#663300", "#6B8E23")      

    # summer
    turtle.tracer(0, 3) #comment out this line if you want to see a fully animated version
    tree(30, 60, branch, branch*0.35, branch*0.02, tt, pen, "#663300", "#539653")      
    turtle.update() #comment out this line if you want to see a fully animated version

    # autumn
    tree(30, 60, branch, branch*0.35, branch*0.02, tt, pen, "#663300", "#B8860B")       
    turtle.update() #comment out this line if you want to see a fully animated version
    time.sleep(1.5)
        
    # winter
    # wipe previous drawings clean
    tt.clear()
    tree(30, 60, branch, branch*0.4, branch*0.3, tt, pen*1.02, "#FFFFFF", "#FFFFFF")
    turtle.update() #comment out this line if you want to see a fully animated version

    # click to exit
    window.exitonclick()

if __name__ == '__main__': main()
   







    