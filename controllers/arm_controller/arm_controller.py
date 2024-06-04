from controller import Robot, Keyboard
robot = Robot()
keyboard = Keyboard()
timestep = 64
keyboard.enable(timestep)

shoulder_lift = robot.getDevice('shoulder_lift_joint')
shoulder_pan = robot.getDevice('shoulder_pan_joint')
elbow = robot.getDevice('elbow_joint')
wrist1 = robot.getDevice('wrist_1_joint')
wrist2 = robot.getDevice('wrist_2_joint')
wrist3 = robot.getDevice('wrist_3_joint')

def move_bot(a=0,b=0,c=0,d=0,e=0,f=0):
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist1.setPosition(d)
    wrist2.setPosition(e)
    wrist3.setPosition(f)
    
move_bot()

shoulder_lift_pos= 0
shoulder_pan_pos = 0
elbow_pos = 0
wrist1_pos = 0
wrist2_pos = 0
wrist3_pos = 0

while robot.step(timestep)!=-1:
    keyPressed=keyboard.getKey()
    print(keyPressed)
    if keyPressed == 317:
        shoulder_lift_pos +=0.01
    elif keyPressed == 315:
        shoulder_lift_pos -=0.01
    elif keyPressed == 316:
        shoulder_pan_pos -=0.01
    elif keyPressed == 314:
        shoulder_pan_pos +=0.01
    elif keyPressed == 87:
        elbow_pos -=0.01
    elif keyPressed == 83:
        elbow_pos +=0.01
    elif keyPressed == 65:
        wrist1_pos +=0.01
    elif keyPressed == 68:
        wrist1_pos -=0.01
    elif keyPressed == 49:
        wrist2_pos +=0.01 
    elif keyPressed == 50:
        wrist2_pos -=0.01 
    elif keyPressed == 51:
        wrist3_pos +=0.01 
    elif keyPressed == 52:
        wrist3_pos -=0.01  
                  
    move_bot(shoulder_lift_pos, shoulder_pan_pos, elbow_pos, wrist1_pos, wrist2_pos, wrist3_pos) 