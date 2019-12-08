
#importing libraries to be used
import matplotlib.pyplot as mpl
#assigning inital values from 0-99
x = list(range(0,100));
y = [None]*100 ;

#looping statement for the function 
for z in range (0,100):
    n=z;
    if n <= 9:
        n= (n**2)-7;
        
    elif n >=10: #if n is not <= 9 
        while n >= 10: #to continue the loop
            n = n-10;
        if n<=9: #if n is <10 it will go back to the first equation
            n = (n**2)-7;
    y[z] = n;
    
#plotting the function using  plt.stem and adding labels to the graph
mpl.stem(x,y,'r-')
mpl.xlabel('n(0-99)')
mpl.ylabel('f(n)')
mpl.title('plot of x and y')
mpl.grid()

# the graph f(n) has only 9 y-axis values. n= 0 to 2 have negative y values
# while n=3 to 9 have postive y values. 