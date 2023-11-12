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
    if rpm ==0:
        calories = 0
        return calories
    else:
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

def new_motor_variable(speed,radius):
    new_rpm=(speed*(5/18))*60/(radius*2*m.pi)
    return new_rpm
