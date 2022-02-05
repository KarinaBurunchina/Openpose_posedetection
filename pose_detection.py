import pandas as pd
from math import sqrt

# Calculate the distance between 2 points
def distance(x0, y0, x1, y1):
    a = sqrt((x1-x0)**2 + (y1-y0)**2)
    return a

#Whether the right arm is straight or not. 
#If (the sum of the distances between Points 2->3 and 3->4 )* 0.8 is less than (the distance between Points 2->4)  
def RightHand_straight(x):
    if (distance(x[7], x[8], x[10], x[11]) + distance(x[10], x[11], x[13], x[14]))* 0.8 < distance(x[7], x[8], x[13], x[14]):
        return True
    else: return False

#Whether the left arm is straight or not. 
#If (the sum of the distances between Points 5->6 and 6->7 )* 0.8 is less than (the distance between Points 5->7)
def LeftHand_straight(x):
    if (distance(x[16], x[17], x[19], x[20]) + distance(x[19], x[20], x[22], x[23]))* 0.8 < distance(x[16], x[17], x[22], x[23]):
        return True
    else: return False

def happy_fun(x):
    #checks if Points 4 and 7 higher than Point 0 + if the arms is straight or close to straight position. 
    #under all conditions to be true , the state is Happy
    if x[14] < x[2] and x[23] < x[2] and RightHand_straight(x) == True and LeftHand_straight(x) == True:
        return True
    else: return False

def fear_fun(x):
    #chechks if Points 4 and 7 higher than Point 3 and 6 respectively + if the arm is close to shoulders. 
    #under all conditions to be true , the state is Fear
    if x[14] < x[11] and x[23] < x[20] and distance(x[13], x[14], x[7], x[8]) < distance(x[13], x[14], x[10], x[11]) and distance(x[22], x[23], x[16], x[17]) < distance(x[22], x[23], x[19], x[20]):
        return True
    else: return False

def disgust_fun(x):
    #chechks if the arms is straight or close to straight position + if they tilted both either to the right or to the left. 
    #under all conditions to be true , the state is Disgust
    if RightHand_straight(x) == True and LeftHand_straight(x) == True:
        if (x[13] > x[10] and x[22] > x[19]) or (x[13] < x[10] and x[22] < x[19]):
            return True
    else: return False

#computes duration of previous state
def dur_fun(time, duration):
    if index != 0:
        duration = time - duration
        if duration >= 1:
            print("       Duration = "+ str(duration)+ " seconds")


happy = 0
disgust = 0
fear = 0
garbage = 0

isHappy = False
isFear = False
isDisgust = False
isGarbage = False

time = 0
frame_num = 0
duration = 0

#change folder on your own
data = pd.read_csv (r'C:\projects\openpose_tutorial\csv\video.csv', skiprows= 0) #skips header


for index, row in data.iterrows():   
    
    # count time as 30 frames per seconds starting from frame with inspected state
    if index % 30 == 0:
        time = time + 1

    # check the Happy state by condition and whether it is not already happy from previous frame
    if happy_fun (row) == True:
        #if the state is activated from previous frame, then skip it.
        if isHappy == True:
            continue
        happy = happy + 1 #count for Happy state
        dur_fun(time, duration)
        print("HAPPY state #" + str(happy))
        duration = time

        isHappy = True
        isFear = False
        isDisgust = False
        isGarbage = False

    elif fear_fun (row) == True:
        # check the Fear state by condition and whether it is not already fear from previous frame
        if isFear == True:
            continue
        dur_fun(time, duration)
        fear = fear + 1 #counts for Fear states
        print("FEAR state #" + str(fear))
        duration = time

        isHappy = False
        isFear = True
        isDisgust = False
        isGarbage = False

    elif disgust_fun(row) == True:
        # check the Disgust state by condition and whether it is not already fear from previous frame
        if isDisgust == True:
            continue
        
        dur_fun(time, duration)
        disgust = disgust + 1 #counts for Disgust states
        print("DISGUST state #" + str(disgust))
        duration = time

        isHappy = False
        isFear = False
        isDisgust = True
        isGarbage = False
    else:
        #if the state is activated from previous frame, then skip it.
        if isGarbage == True:
            continue
        dur_fun(time, duration)
        garbage = garbage + 1
        print("Garbage state #" + str(garbage))
        duration = time

        isHappy = False
        isFear = False
        isDisgust = False
        isGarbage = True




        
