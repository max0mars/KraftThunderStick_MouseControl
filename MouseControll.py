import serial
import mouse

# brown is x
# Orange is y
# Black is slide

fast = 60
medium = 25
slow = 5

s = serial.Serial('COM3')

res = ""
x = 15
run = True

last = 1

def flip():
    global run 
    run = False
    print("Exit")


def moveMouse(v):
    x = 0
    y = 0
    #Right:
    #Fast: <450, Medium < 500, Slow < 600
    #Left:
    #Fast >1000, Medium >800 , Slow >650
    if v[0] < 450:
        #fast right
        x = fast
    elif v[0] < 500:
        #medium right
        x = medium
    elif v[0] < 600:
        #slow right
        x = slow
    elif v[0] > 1000:
        #fast left
        x = -fast
    elif v[0] > 800:
        #medium left
        x = -medium
    elif v[0] > 650:
        #slow left
        x = -slow
    

    #Down:
    #Slow <570, Medium <490, Fast <445
    #Up:
    #Slow >650, Medium >750, Fast >850
    if v[1] < 445:
        #fast down
        y = fast
    elif v[1] < 490:
        #medium down
        y = medium
    elif v[1] < 570:
        #slow down
        y = slow
    elif v[1] > 850:
        #fast up
        y = -fast
    elif v[1] > 750:
        #medium up
        y = -medium
    elif v[1] > 650:
        #slow up
        y = - slow

    mult = v[2] / 500
    if v[2] > 1000:
        mult = 4


    global last 
    if(v[3] == 0 and v[3] != last):
        mouse.press("left")
    if(v[3] == 1):
        mouse.release("left")
    
    last = v[3]
    #print(str(v[0]) + ", " + str(v[1]) + ", " + str(v[3]))
    mouse.move(x*mult, y*mult, False)




mouse.on_right_click(flip)
myString = ""
while run:
    reading = True
    #while reading:
    readIn = ""
    try: 
        readIn = s.read().decode()
    except:
        print("Unknown Char")
    
    
    myString += readIn
    if(readIn == "\n"):
        vals = myString.split()#[0] = x, [1] = y, [2] = slide, [4] = button
        vals_i = [int(i) for i in vals]
        myString = ""
        moveMouse(vals_i)