# python MS1_128_code.py
# Treadmill Dash Board

import argparse
import math as m

# Define functions

# Function to calculate speed.
def speedclc(rpm,radius):
    '''
    Function to calcuate the speed in 'km/h' by using given rpm value and radius in 'm'.
    '''

    Speed = radius * ((rpm * 2*m.pi)/60)
    return Speed

# Function to calculate distance walked or ran
def distanceclc(rpm,radius,time):
    '''
    Function to calculate the distance in 'km' by using given rpm value and radius in 'm' 
    '''
    
    Distance = speedclc(rpm,radius) * time
    return Distance 

# Function to calculate calories burnt
def caloriesclc(weight,height,rpm,radius,time):
    '''
    Function to calculate the calories by using given rpm value, radius in 'm',time in 'minutes', weight in 'kg' and height in 'm'
    '''
    
    calories = ( (0.035*weight) + ((speedclc(rpm,radius)**2/height)*0.029*weight) ) * (time/60)
    return calories
    

# Function for calculate nomber of steps taken
def stepsclc(height,rpm,radius,time):
    '''
    Function to calcutale the steps by using given rpm value, radius in 'm', time in 'minutes' and height in 'm'
    '''
    gaps = (height*0.414)/2
    steps = distanceclc(rpm,radius,time)/gaps
    return steps

# Function to convert input radius and height into meters.
def meter(string_value):
    lst = string_value.split(' ')
    
    if lst[-1] == 'm':
        return float(lst[0])
    
    elif lst[-1] == 'cm':
        return float(lst[0])/100
    
    elif lst[-1] == 'in':
        return float(lst[0])*0.0254
            
# Function to convert input weight into kilograms.
def kilograme(string_value):
    lst = string_value.split(' ')

    if lst[-1] == 'kg':
        return float(lst[0])
    
    elif lst[-1] == 'lb':
        return float(lst[0])*0.453592

# Function to convert input time into seconds.  
def second(string_value):
    lst = string_value.split(' ')

    if lst[-1] == 'h':
        return float(lst[0])*3600
    
    elif lst[-1] == 'min':
        return float(lst[0])*60
    
    elif lst[-1] == 's':
        return float(lst[0])
    
# input format    
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=3)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
    args.add_argument("--time", type=str, dest="time", help="EXAMPLE: 1 h", default="1 h")
    
    args=args.parse_args()


    # convert inputs into SI
    rpm       = float(args.motor_rate)
    radius_m  = meter(args.radius)
    weight_kg = kilograme(args.weight)
    height_m  = meter(args.height)
    time_s    = second(args.time)

    # find necessary outputs
    speed = speedclc(rpm,radius_m)
    distance = distanceclc(rpm,radius_m,time_s)
    calories = caloriesclc(weight_kg,height_m,rpm,radius_m,time_s)
    steps = stepsclc(height_m,rpm,radius_m,time_s)

    # print the output
    print(int(speed),'m/s')
    print(int(distance),'m')
    print(int(calories),'cal')
    print(int(steps))
    
    




    
