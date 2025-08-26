"""
if letter == "":
    t.up()
    t.goto(0,0)
    t.setheading(0)
    t.forward(Forward)
    t.down()
    
    Forward += 200
"""

import turtle, random, time
t=turtle.Turtle()
def Draw():
    global t
    t.clear()
    turtle.delay(0)
    turtle.Screen().update()
    turtle.speed("fastest")
    Forward = -600
    t=turtle.Turtle()
    t.hideturtle()
    for letter in word.lower():
        if letter == "a":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.down()
            for i in range(130):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(45):
                t.forward(1)
                t.right(2)
            for i in range(170):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            t.forward(25)
            t.left(120)
            t.down()
            for i in range(130):
                t.forward(1)
                t.right(0.4)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(130):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            
            for i in range(137):
                t.forward(1)
                t.right(0.4)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            Forward += 300
        
        if letter == "b":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.down()
            t.right(90)
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.left(90)
            for i in range(50):
                t.forward(1)
            for i in range(250):
                t.forward(1)
                t.left(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            Forward += 200
        
        if letter == "c":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.forward(150)
            t.right(180)
            t.down()
            for i in range(360):
                t.forward(1)
                t.left(0.5)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            
            Forward += 200    
        
        if letter == "d":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.forward(50)
            t.right(90)
            t.down()
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(90)
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(250):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            
            Forward += 200
        if letter == "e":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.forward(180)
            t.right(90)
            t.forward(150)
            t.right(45)
            t.down()
            for i in range(550):
                t.forward(1)
                t.right(0.5)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(25):
                t.forward(3)
                t.right(5)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(180):
                t.forward(1)
                t.right(0.2)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            
            Forward += 200
        
        if letter == "f":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.forward(100)
            t.right(90)
            t.forward(200)
            t.right(180)
            t.down()
            for i in range(175):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(90):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(90)
            t.forward(60)
            t.right(90)
            t.down()
            for i in range(175):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            Forward += 350
        if letter == "g":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.forward(230)
            t.right(180)
            t.down()
            for i in range(210):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(200):
                t.forward(1)
                t.left(0.8)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            for i in range(200):
                t.forward(1)
                t.left(0.2)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            for i in range(200):
                t.forward(1)
                t.left(0.8)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            t.up()
            t.forward(180)
            t.left(90)
            t.forward(137)
            t.down()
            for i in range(50):
                t.forward(1)
                t.left(0.2)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            t.right(100)
            for i in range(200):
                t.forward(1)
                t.left(0.8)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            for i in range(200):
                t.forward(1)
                t.left(0.2)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            for i in range(170):
                t.forward(1)
                t.left(0.8)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            for i in range(210):
                t.forward(1)
                t.left(0.25)
                t.left(random.randrange(0,2))
                t.right(random.randrange(0,2))
            Forward += 350
        if letter == "h":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.right(90)
            t.down()
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            for i in range(30):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.down()
            for i in range(180):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(30):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            Forward += 200
        if letter == "i":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.right(90)
            t.forward(30)
            t.down()
            t.left(90)
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(90)
            for i in range(170):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(90)
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(180)
            for i in range(100):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(180)
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(90)
            t.forward(185)
            t.down()
            for i in range(15):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            Forward += 200
        if letter == "j":
            t.up()
            t.goto(0,0)
            t.setheading(0)    
            t.forward(Forward)
            t.right(90)
            t.forward(30)
            t.down()
            t.left(90)
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(90)
            for i in range(170):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(45):
                t.forward(1)
                t.right(2)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(30):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            t.forward(50)
            t.left(90)
            t.forward(185)
            t.down()
            for i in range(15):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
    
            Forward += 200
        if letter == "k":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.down()
            t.right(90)
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            for i in range(70):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.down()
            t.right(90)
            t.forward(1)
            for i in range(70):
                t.up()
                t.right(90)
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
                t.left(90)
                t.down()
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(180)
            for i in range(70):
                t.up()
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
                t.right(90)
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
                t.left(90)
            t.down()
            t.right(180)
            t.forward(1)
            for i in range(70):
                t.up()
                t.left(90)
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
                t.right(90)
                t.down()
                t.forward(1)  
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))          
            
            
            Forward += 200
            
        if letter == "l":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward+50)
            t.down()
            for i in range(40):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(90)
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(90)
            for i in range(50):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(180)
            for i in range(100):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            
            
            Forward += 200
        if letter == "m":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.right(90)
            t.forward(60)
            t.down()
            for i in range(140):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(45)
            t.down()
            for i in range(90):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            t.right(45)
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(45)
            t.down()
            for i in range(90):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            t.right(45)
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            
            
            Forward += 200
        if letter == "n":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.right(90)
            t.forward(60)
            t.down()
            for i in range(140):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.right(45)
            t.down()
            for i in range(180):
                t.forward(1)
                t.right(0.5)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            t.right(45)
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            
            Forward += 200
        if letter == "o":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.right(90)
            t.forward(150)
            t.down()
            for i in range(360):
                t.forward(1)
                t.left(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            
            
            Forward += 200
            
        if letter == "p":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.down()
            t.right(90)
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.up()
            t.right(180)
            t.forward(100)
            t.down()
            t.right(90)
            for i in range(30):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(160):
                t.forward(1)
                t.left(10/9)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(45):
                t.forward(1)
                t.left(0.5)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            
            
            Forward += 200
        
        if letter == "q":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward+100)
            t.right(90)
            t.forward(200)
            t.right(180)
            t.down()
            for i in range(200):
                t.forward(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            t.left(90)
            for i in range(50):
                t.forward(1)
            for i in range(250):
                t.forward(1)
                t.left(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            Forward += 200
            
        if letter == "r":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward)
            t.right(90)
            t.forward(75)
            t.down()
            for i in range(125):
                t.forward(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            t.up()
            t.right(180)
            t.forward(100)
            t.down()
            t.right(45)
            for i in range(90):
                t.forward(1)
                t.right(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            
            Forward += 200
        
        if letter == "s":
            t.up()
            t.goto(0,0)
            t.setheading(0)
            t.forward(Forward+150)
            t.down()
            t.right(180)
            for i in range(125):
                t.forward(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(160):
                t.forward(1)
                t.left(1)
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(120):
                t.forward(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            for i in range(160):
                t.forward(1)
                t.right(1) 
                t.left(random.randrange(0,3))
                t.right(random.randrange(0,3))
            for i in range(125):
                t.forward(1)
                t.left(random.randrange(0,5))
                t.right(random.randrange(0,5))
            Forward += 200
    


def Answer(ans):
    global i
    global title
    global word
    global answ
    global t
    if i == 0:
        if ans == "y":
            title = "Go Again?(Y/N): "
            tt.clear()
            words = open("AllEnglishWords.txt","r")
            i=random.randrange(1,len(words.readlines())+1)
            words = open("AllEnglishWords.txt","r")
            j=0
            while j < i:
                j+=1
                word = words.readline()
            if word[-1] == "\n":
                word = word[:-1]
            #print(word)
            temp = ""
            for x in word:
                if x in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]:
                    temp += x
            word = temp
            #word = "s"
            Draw()
            i = 1
        else:
            tt.clear()
            tt.goto(0,0)
            tt.write("Good Bye",font=("Arial",40,"normal"),align="center")
            tt.up()
            tt.forward(100000)
            tt.right(180)
            tt.forward(100000)
            tt.right(180)            
            i=-1
    elif i == 1:
        if ans == "y":
            Draw()
        else:
            i = 2
    elif i == 2:
        if ans == "1":
            if answ == word:
                tt.clear()
                turtle.Screen().update()
                tt.goto(0,-150)
                tt.write("You Got It!",font=("Arial",40,"normal"),align="center")
                tt.up()
                tt.forward(100000)
                tt.right(180)
                tt.forward(100000)
                tt.right(180)
                tt.goto(0,0)
                i = 0
            else:
                tt.clear()
                turtle.Screen().update()
                tt.goto(0,-150)
                tt.write("Nope, TryAgain",font=("Arial",40,"normal"),align="center")
                tt.goto(0,0)
                tt.up()
                tt.forward(100000)
                tt.right(180)
                tt.forward(100000)
                tt.right(180)
            answ = ""
        elif ans == "2":
            tt.clear()
            turtle.Screen().update()
            tt.goto(0,-150)
            tt.write("So Close, the Word was "+word,font=("Arial",40,"normal"),align="center")
            tt.up()
            tt.forward(1000000)
            tt.right(180)
            tt.forward(1000000)
            tt.right(180)
            tt.goto(0,0)
            i = 0            
            
        else:
            answ += ans
    else:
        pass
    

turtle.setup()
turtle.screensize(100000,100000,"white")
turtle.Screen().setup(width=1.0, height=1.0)
tt=turtle.Turtle()
tt.hideturtle()
i = 0
answ = ""
word = ""
title = "Begin?(Y/N)"


turtle.onkey(lambda: Answer("y"),"y")
turtle.onkey(lambda: Answer("y"),"Y")
turtle.onkey(lambda: Answer("n"),"n")
turtle.onkey(lambda: Answer("n"),"N")
turtle.onkey(lambda: Answer("a"),"a")
turtle.onkey(lambda: Answer("a"),"A")

turtle.onkey(lambda: Answer("b"),"b")
turtle.onkey(lambda: Answer("b"),"B")

turtle.onkey(lambda: Answer("c"),"c")
turtle.onkey(lambda: Answer("c"),"C")

turtle.onkey(lambda: Answer("d"),"d")
turtle.onkey(lambda: Answer("d"),"D")

turtle.onkey(lambda: Answer("e"),"e")
turtle.onkey(lambda: Answer("e"),"E")

turtle.onkey(lambda: Answer("f"),"f")
turtle.onkey(lambda: Answer("f"),"F")

turtle.onkey(lambda: Answer("g"),"g")
turtle.onkey(lambda: Answer("g"),"G")

turtle.onkey(lambda: Answer("h"),"h")
turtle.onkey(lambda: Answer("h"),"H")

turtle.onkey(lambda: Answer("i"),"i")
turtle.onkey(lambda: Answer("i"),"I")

turtle.onkey(lambda: Answer("j"),"j")
turtle.onkey(lambda: Answer("j"),"J")

turtle.onkey(lambda: Answer("k"),"k")
turtle.onkey(lambda: Answer("k"),"K")

turtle.onkey(lambda: Answer("l"),"l")
turtle.onkey(lambda: Answer("l"),"L")

turtle.onkey(lambda: Answer("m"),"m")
turtle.onkey(lambda: Answer("m"),"M")

turtle.onkey(lambda: Answer("n"),"n")
turtle.onkey(lambda: Answer("n"),"N")

turtle.onkey(lambda: Answer("o"),"o")
turtle.onkey(lambda: Answer("o"),"O")

turtle.onkey(lambda: Answer("p"),"p")
turtle.onkey(lambda: Answer("p"),"P")

turtle.onkey(lambda: Answer("q"),"q")
turtle.onkey(lambda: Answer("q"),"Q")

turtle.onkey(lambda: Answer("r"),"r")
turtle.onkey(lambda: Answer("r"),"R")

turtle.onkey(lambda: Answer("s"),"s")
turtle.onkey(lambda: Answer("s"),"S")

turtle.onkey(lambda: Answer("t"),"t")
turtle.onkey(lambda: Answer("t"),"T")

turtle.onkey(lambda: Answer("u"),"u")
turtle.onkey(lambda: Answer("u"),"U")

turtle.onkey(lambda: Answer("v"),"v")
turtle.onkey(lambda: Answer("v"),"V")

turtle.onkey(lambda: Answer("w"),"w")
turtle.onkey(lambda: Answer("w"),"W")

turtle.onkey(lambda: Answer("x"),"x")
turtle.onkey(lambda: Answer("x"),"X")

turtle.onkey(lambda: Answer("y"),"y")
turtle.onkey(lambda: Answer("y"),"Y")

turtle.onkey(lambda: Answer("z"),"z")
turtle.onkey(lambda: Answer("z"),"Z")

turtle.onkey(lambda: Answer("1"),"1")
turtle.onkey(lambda: Answer("2"),"2")
turtle.listen()


try:
    while True:    
        if i == 0:
            tt.clear()
            turtle.Screen().update()
            tt.goto(0,0)
            tt.write(title,font=("Arial",40,"normal"),align="center")
            tt.up()
            tt.forward(100000)
            tt.right(180)
            tt.forward(100000)
            tt.right(180)                        
        if i == 1:
            tt.clear()
            turtle.Screen().update()
            tt.goto(0,0)
            tt.write("ReDraw?",font=("Arial",40,"normal"),align="center") 
            tt.up()
            tt.forward(100000)
            tt.right(180)
            tt.forward(100000)
            tt.right(180)                        
        if i == 2:
            tt.clear()
            turtle.Screen().update()
            tt.goto(0,0)
            tt.write("Guess The Word! (Press 1 to Submit, 2 to Give Up)",font=("Arial",40,"normal"),align="center")
            tt.up()
            tt.forward(100000)
            tt.right(180)
            tt.forward(100000)
            tt.right(180)                        
        if i == -1:
            turtle.Screen().clear()
            
            break
    turtle.exitonclick()
        
except:
    pass
