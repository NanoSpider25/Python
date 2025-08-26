import turtle, random, time
turtle.screensize(2000,2000,"white")
def keyboard(c):
    global keyb
    keyb = turtle.Turtle()
    keyb.goto(-250,150)
    for a in range(len(alph)):
        c = colors[a]
        if c == "grey":
            l = "white"
        else:
            l = "black"        
        if a > 14:
            SmallBox(keyb,x,y)
        

def SmallBox(b,x,y):
    turtle.tracer(False)
    b.hideturtle()
    b.up()
    b.goto(x,y)
    b.down()
    b.setheading(0)
    b.right(90)
    b.up()
    b.forward(25)
    b.right(180)
    b.down()
    b.begin_fill()
    for i in range(9):
        b.forward(1)
        b.right(10)
    b.forward(10)
    for i in range(9):
        b.forward(1)
        b.right(10)
    b.forward(20)
    for i in range(9):
        b.forward(1)
        b.right(10)
    b.forward(10)
    for i in range(9):
        b.forward(1)
        b.right(10)
    b.forward(20)
    keys.append(b)
    b.end_fill()
    turtle.tracer(True)
    
def Box(b):
    turtle.tracer(False)
    b.hideturtle()
    b.up()
    b.goto(TopX,TopY)
    b.down()
    b.setheading(0)
    b.right(90)
    b.up()
    b.forward(25)
    b.right(180)
    b.down()
    b.begin_fill()
    for i in range(4):
        for i in range(9):
            b.forward(1)
            b.right(10)
        b.forward(50)
    Boxes.append(b)
    b.end_fill()
    turtle.tracer(True)
    
def Write(x,y,l):
    global TopX
    global TopY    
    global w
    global count
    global ans
    global Lines
    if x < 200:
        turtle.tracer(False)
        w = turtle.Turtle()
        w.hideturtle()
        w.up()
        w.goto(x,y)
        w.setheading(0)
        w.left(90)
        w.down()
        w.write(l,align="center",font=("Tahoma",40,"normal"))
        TopX += 80
        Letters.append(w)
        count += 1
        ans += l
        Lines += 1
        
        
def BackSpace():
    global TopX
    global TopY
    global count
    global ans
    global Lines
    global n
    global click
    click = 0
    if TopX > -200:
        try:
            n.clear()
        except:
            pass
        Letters[count].clear()
        Letters.pop()
        TopX -= 80
        count -= 1
        ans = ans[:len(ans)-1]
        Lines -= 1
    
def Enter():
    global TopX
    global TopY    
    global ans
    global Lines
    global Letters
    global count
    global word
    global n
    global click
    global e
    click += 1
    #Conditions
    tFive = open("AllEnglishWords5.txt","r")
    lent = len(tFive.readlines())+1
    tFive = open("AllEnglishWords5.txt","r")
    i = 0
    bWin = False
    bLose = False
    ans = ans.lower()
    while True:
        if ans == word:
            bWin = True
            TopX -= 400
            for k in range(5):
                Boxes[Lines].color("#76EE00")
                Box(Boxes[Lines])
                #print(k)
                Letters[k].color("white")
                Letters[k].write(ans[k].upper(),align="center",font=("Tahoma",40,"normal"))     
                TopX += 80
            break
        i += 1
        if i == lent:
            break
        wordd = tFive.readline()[:5]
        print(wordd)
        if (ans == wordd) and (TopY > -175):
            
            wordb = word
            TopX -= 400
            for k in range(5):
                Boxes[Lines].fillcolor("grey")
                Box(Boxes[Lines])
                Letters[k].color("white")
                Letters[k].write(ans[k].upper(),align="center",font=("Tahoma",40,"normal"))
                TopX += 80
                
                
            Green = []
            for l in range(5):
                TopX -= 400
                bG = False
                for m in range(5):
                    if ans[m] == wordb[l]:
                        if m == l:
                            #turtle.tracer(True)
                            Boxes[Lines].fillcolor("#76EE00")
                            Box(Boxes[Lines])
                            #turtle.tracer(True)
                            Letters[m].color("white")
                            Letters[m].write(ans[m].upper(),align="center",font=("Tahoma",40,"normal"))
                            bG = True
                    TopX += 80
                if bG:
                    Green.append(ans[l])
                else:
                    Green.append("")
                        
                
                
                
            """
            for x in range(len(Green)):
                print(wordb[x],Green[x])
                if wordb[x] == Green[x]:#slp o
                    if x < 4:
                        wordb = wordb[:x] + " " + wordb[x+1:]
                        print(wordb)
                    else:
                        wordb += " "
            """
            
                    
            #temp = word
            #wordc = word
           # print(temp)
            j = 0
            for j in range(5):
                TopX -= 400
                for k in range(5):
                    if ans[k] != Green[k]:
                        if (ans[k] == wordb[j]):#lpeo
                            wordb = wordb[:j] + " " + wordb[j+1:]
                            Boxes[Lines].fillcolor("orange")
                            Box(Boxes[Lines])
                            Letters[k].color("white")
                            Letters[k].write(ans[k].upper(),align="center",font=("Tahoma",40,"normal"))
                    TopX += 80
                j += 1
                
                
                
            #word = temp
           # print(len(word))
            
                
            Letters = []
            count = -1
            TopX -= 400
            TopY -= 80
            click = 0
            break
        elif (TopY == -175) and (ans == wordd):
            bLose = True
            break
    #time.sleep(1)
    if i == 15921:
        if click == 1:
            n = turtle.Turtle()
            n.up()
            n.goto(0,215)
            n.hideturtle()
            n.write("Not in word list",align="center",font=("Tahoma",40,"normal"))
            i = 0
        #print(count)
    if bWin:
        time.sleep(1)
        for a in Letters:
            a.clear()
        for b in Boxes:
            b.clear()
        e = turtle.Turtle()
        e.up()
        e.hideturtle()
        e.goto(0,100)
        e.write("The Word was",align="center",font=("Tahoma",40,"normal"))
        e.goto(0,-50)
        e.write(word.upper(),align="center",font=("Georgia",100,"bold"))
        time.sleep(2)
        Begin()
    if bLose:
        time.sleep(1)
        for a in Letters:
            a.clear()
        for b in Boxes:
            b.clear()
        e = turtle.Turtle()
        e.up()
        e.hideturtle()
        e.goto(0,100)
        e.write("The Word was",align="center",font=("Tahoma",40,"normal"))
        e.goto(0,-50)
        e.write(word.upper(),align="center",font=("Georgia",100,"bold"))  
        time.sleep(2)
        Begin()
    ans = ""
        
        
        
def Begin():
    global Letters
    global ans
    global count
    global word
    global TopX
    global TopY
    global Boxes
    global Lines
    global click
    global e
    #time.sleep(1)
    e.clear()
    click = 0
    keys = []
    Boxes = []
    Letters = []
    ans = ""
    Lines = -1
    count = -1
    tFive = open("AllEnglishWords5.txt","r")
    num = random.randrange(1,5758)
    i = 0
    while True:
        i += 1
        word = tFive.readline()
        if i == num:
            break
    word = word[:5]
    #word = "gitim"
    print(word)
    TopX,TopY = -200,225
    
    for j in range(6):
        for i in range(5):
            b = turtle.Turtle()      
            b.fillcolor("white")
            Box(b)
            TopX += 80
        TopX -= 400
        TopY -= 80
    TopX,TopY = -200,225 
    bBegin = False
    

e = turtle.Turtle()
e.hideturtle()
Begin()
turtle.onkey(lambda: Write(TopX+28,TopY-80,"q".upper()),"q")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"w".upper()),"w")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"e".upper()),"e")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"r".upper()),"r")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"t".upper()),"t")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"y".upper()),"y")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"u".upper()),"u")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"i".upper()),"i")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"o".upper()),"o")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"p".upper()),"p")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"a".upper()),"a")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"s".upper()),"s")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"d".upper()),"d")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"f".upper()),"f")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"g".upper()),"g")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"h".upper()),"h")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"j".upper()),"j")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"k".upper()),"k")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"l".upper()),"l")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"z".upper()),"z")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"x".upper()),"x")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"c".upper()),"c")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"v".upper()),"v")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"b".upper()),"b")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"n".upper()),"n")
turtle.onkey(lambda: Write(TopX+28,TopY-80,"m".upper()),"m")
#turtle.onkey(Begin,"S")
turtle.onkey(BackSpace,"BackSpace")
turtle.onkey(Enter,"Return")
turtle.listen()
turtle.done()