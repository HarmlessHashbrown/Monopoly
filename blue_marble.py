import turtle
import time
from PIL import Image, ImageTk
import random
'''
[game_stadium  function description]
it makes up the base board of the game and includes how the
dice number changes to inform the players.
'''
def game_stadium(x,y):
    global colors
    turtle.tracer(False)
    pen.goto(-240,240)
    pen.setheading(0)
    pen.color('orange')
    pen.begin_fill()
    for i in range(4):
        pen.forward(480)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(0,-70)
    pen.color("white")
    pen.begin_fill()
    for i in range(2):
        pen.forward(100)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.goto(50,-103)
    pen.color("black")
    pen.write("roll",font=("arial",15,"bold"),align="center")
    pen.hideturtle()
    pen.goto(-390,-385)
    pen.pendown()
    pen.setheading(0)
    for j in range(4):
        pen.begin_fill()
        pen.color('black')
        for i in range(2):
            pen.forward(185)
            pen.left(90)
            pen.forward(65)
            pen.left(90)
        pen.color(colors[j])
        pen.end_fill()
        pen.penup()
        pen.forward(195)
        pen.pendown()
    pen.penup()
    money()
    turtle.tracer(True)

'''
[Dice Function description]
this imports the x and y coordinates of where the mouse was clicked,
ultimatley when aligned with the right x and y coordinates, will
result in the dice function to be enabled.
'''
def dice(x,y):
    global pen, card_stat, card_turtle, turn, country_orders, roll, player_info
    num1 = random.randint(1,6) 
    #num1 = 14
    num2 = random.randint(1,6)
    turtle.tracer(False)
    #card stat allows the player to know that the card function has been enabled which allows them to buy or pass the land they are on.
    if card_stat == True:
        if -90<x<-10 and -60>y>-160:
            curr_cou = country_orders[player_info['moves'][turn]]
            if player_info['money'][turn] - board[curr_cou]['price']>=0:
                player_info['money'][turn] = player_info['money'][turn] - board[curr_cou]['price']
                print(player_info)
                #money()
                own(curr_cou)
                turns()
            else:
                print("SELLLLL")
                sell()
            card_turtle.clear()
            card_stat = False
            
        if 10<x<90 and -60>y>-160:
            print('pass')
            card_turtle.clear()
            card_stat = False
            turns()
        return None
    #roll allows the player to click the roll button when it is their turn, and draws it so that the player knows how far they are going
    if roll == True:
        if 0<x<100 and -70>y>-120:
            print('roll')
            roll = False
            '''
            This code allows the game to know when the players can be freed
            from the island.
            '''
            if player_info['island'][turn]>0:
                player_info['island'][turn]-=1
                print(player_info['island'])
                rest()
                turns()
                return None
            pen.setheading(0)
            dices={1:[[25,-35]],
                2:[[16,-35],[34,-35]], 
                3:[[12,-35],[25,-35],[38,-35]],
                4:[[15,-22],[15,-48],[35,-22],[35,-48]],
                5:[[15,-22],[15,-48],[35,-22],[35,-48],[25,-35]],
                6:[[15,-22],[15,-35],[15,-48],[35,-22],[35,-35],[35,-48]],
                14:[[15,-22],[15,-35],[15,-48],[35,-22],[35,-35],[35,-48]],}
            pen.goto(0,-10)
            pen.color('white')
            pen.begin_fill()
            for i in range(4):
                pen.forward(50)
                pen.right(90)
            pen.end_fill()
            pen.shape("circle")
            pen.color("black")
            pen.penup()
            pen.shapesize(0.5)
            for p in dices[num1]:
                pen.goto(p)
                pen.stamp()
            turtle.tracer(True)
            character(num1)
        '''
        dices2={1:[[80,-35]],
            2:[[71,-35],[89,-35]], 
            3:[[67,-35],[80,-35],[93,-35]],
            4:[[70,-22],[70,-48],[90,-22],[90,-48]],
            5:[[70,-22],[70,-48],[90,-22],[90,-48],[80,-35]],
            6:[[70,-22],[70,-35],[70,-48],[90,-22],[90,-35],[90,-48]]}
        pen.color("white")
        pen.goto(55,-10)
        pen.begin_fill()
        for i in range(4):
            pen.forward(50)
            pen.right(90)
        pen.end_fill()
        for p in dices2[num2]:
            pen.goto(p)
            pen.color("black")
            pen.stamp()
        '''
'''
[Travel Function description]
it is the function that brings up the message on rather to
travel or not when you reach the rocket.
'''
def travel():
    global traveler_pen,players
    traveler_pen.color('white')
    traveler_pen.penup()
    traveler_pen.speed(0)
    traveler_pen.setheading(0)
    traveler_pen.goto(-400,-400)
    traveler_pen.begin_fill()
    for i in range(4):
        traveler_pen.forward(800)
        traveler_pen.left(90)
    traveler_pen.end_fill()

    traveler_pen.goto(-20,-290)
    traveler_pen.setheading(90)
    traveler_pen.color('red')
    traveler_pen.begin_fill()
    for i in range(2):
        traveler_pen.forward(400)
        traveler_pen.left(90)
        traveler_pen.forward(250)
        traveler_pen.left(90)
    traveler_pen.end_fill()
    traveler_pen.goto(-145,-90)
    traveler_pen.color("white")
    traveler_pen.write("Go",font = ("arial",30,"bold"),align="center")
    traveler_pen.goto(20,-290)
    traveler_pen.setheading(90)
    traveler_pen.color('blue')
    traveler_pen.begin_fill()
    for i in range(2):
        traveler_pen.forward(400)
        traveler_pen.right(90)
        traveler_pen.forward(250)
        traveler_pen.right(90)
    traveler_pen.end_fill()
    traveler_pen.goto(145,-90)
    traveler_pen.color("white")
    traveler_pen.write("Skip",font = ("arial",30,"bold"),align = "center")
    traveler_pen.goto(0,200)
    traveler_pen.color('black')
    traveler_pen.write("Would you like to go to ANY COUNTRY you want?",font = ("arial",25,"bold"),align='center')
    players[0].hideturtle()
    players[1].hideturtle()
    players[2].hideturtle()
    players[3].hideturtle()
    turtle.onscreenclick(travel_select)
'''
[Travel_Select Function description]
it is the function that allows the player to see the wording
"Click to an area you want to travel to!" which gives the player
an idea that they need to clikc on the country they want to travel to
'''
def travel_select(x,y):
    global traveler_pen,players
    print(f"go & pass click : {x},{y}")
    if 20 < x < 270 and -290 < y < 110:
        traveler_pen.clear()
        turtle.onscreenclick(dice)
        for i in range(4):
            players[i].showturtle()
        turns()
    elif -270 < x < -20 and -290 < y < 110:
        traveler_pen.clear()
        traveler_pen.goto(-240,240)
        traveler_pen.color("white")
        traveler_pen.setheading(0)
        traveler_pen.begin_fill()
        for i in range(4):
            traveler_pen.forward(480)
            traveler_pen.right(90)
        traveler_pen.end_fill()
        traveler_pen.goto(0,0)
        traveler_pen.color('black')
        traveler_pen.write('Click to an area you want to travel to!',font = ('arial',20,'bold'),align = 'center')
        turtle.onscreenclick(finder)
def choose_sell(x,y):
    global player_info,turn,sell_turtle
    if -210<x<-20 and -220<y<180:
        print("yes")
        sell_turtle.clear()
        sell_turtle.goto(95,170)
        sell_turtle.setheading(270)
        for i in range(len(player_info['own'][turn])):
            sell_turtle.write(player_info['own'][turn][i],font=('arial',20,'bold'))
            sell_turtle.forward(30)
            sell_turtle.write(f"bought:{board[player_info['own'][turn][i]]['price']} sold:{board[player_info['own'][turn][i]]['price']/2}"  ,font=('arial',20,'bold'))
            sell_turtle.forward(30)
        turns()
    elif 20<x<210 and -220<y<180:
        print('no')
        sell_turtle.clear()
        turtle.onscreenclick(dice)
        turns()
    #player_info['own'][turn]

def sell():
    global sell_turtle
    sell_turtle.showturtle()
    sell_turtle.penup()
    sell_turtle.color("red")
    sell_turtle.goto(250,300)
    sell_turtle.pendown()
    sell_turtle.pensize(3)
    sell_turtle.setheading(270)
    sell_turtle.begin_fill()
    for _ in range(2):
        sell_turtle.forward(600)
        sell_turtle.right(90)
        sell_turtle.forward(500)
        sell_turtle.right(90)
    sell_turtle.color('white')
    sell_turtle.end_fill()
    sell_turtle.color('red')
    sell_turtle.penup()
    sell_turtle.goto(0,250)
    sell_turtle.hideturtle()
    sell_turtle.write("YOU DON'T HAVE ENOUGH MONEY",font = ('arial',20,'bold'),align='center')
    sell_turtle.goto(0,220)
    sell_turtle.write("WILL YOU SELL ONE OF YOU LAND TO BUY THIS?",font = ('arial',20,'bold'),align='center')
    sell_turtle.goto(-210,180)
    sell_turtle.pendown()
    sell_turtle.setheading(0)
    sell_turtle.color("green")
    for j in range(2):
        sell_turtle.forward(200)
        sell_turtle.right(90)
        sell_turtle.forward(400)
        sell_turtle.right(90)
        sell_turtle.forward(200)
        sell_turtle.right(90)
        sell_turtle.forward(400)
        sell_turtle.right(90)
        sell_turtle.penup()
        sell_turtle.forward(220)
        sell_turtle.pendown()
        sell_turtle.color('red')
    sell_turtle.penup()
    sell_turtle.color("green")
    sell_turtle.goto(-105,-20)
    sell_turtle.write("Yes",font = ('arial',30,"bold"),align="center")
    sell_turtle.color('red')
    sell_turtle.goto(105,-20)
    sell_turtle.write("No",font = ('arial',30,"bold"),align="center")
    turtle.onscreenclick(choose_sell)
'''
[Finder Function description]
It is the function that allows the player to click on a country and
makes the turtle move to that specific area
'''
def finder(x,y):
    global country_orders,traveler_pen
    no_owner = [0,7,14,21,4,18,25]
    goto = int(abs((x-240)//80))
    if -320 < y < -240 and -320 < x < 320:
        goto = int(abs((x-240)//80))
    elif 240 < y < 320 and -320 < x < 320:
        goto = (7-goto)+ 14 
    elif -320 < x < -240 and -320 < y < 320:
        goto = int((abs((y+320)//80))+7)
    elif 240 < x < 320 and -240 < y < 320:
        goto = int((abs((y-240)//80)))+21

    for i in range(4):
        players[i].showturtle()
    traveler_pen.clear()
    
    if goto-21 >=0:
        character(goto-21)
    elif goto-21 < 0:
        character(goto+7)
    turtle.onscreenclick(dice)
'''
[Island Function description]
This function tells the player whether they are at the island so 
the code above can skip their turn 3 times.
'''      
def island():
    global turn,player_info
    player_info['island'][turn]=3
    print(player_info['island'])
    rest()
    turns()
'''
[Rest Function description]
This function allows the players to see how many turns they have left until escaping the island
'''          
def rest():
    global rest_pen, player_info, turn, colors
    #turtle.tracer(False)

    rest_pen.penup()
    rest_pen.setheading(-180)
    rest_pen.goto(-190,-150)
    rest_pen.color('#19054a')
    rest_pen.begin_fill()
    for i in range(2):
        rest_pen.circle(35,180) 
        rest_pen.forward(140)
    rest_pen.end_fill()
    rest_pen.goto(-185,-190)
    rest_pen.setheading(0)
    for i in range(4):
        rest_pen.color(colors[i])
        rest_pen.stamp()
        rest_pen.setheading(90)
        rest_pen.forward(10)
        rest_pen.write(f"{player_info['island'][i]}", font=('arial',20,"bold"), align='center')
        rest_pen.backward(10)
        rest_pen.setheading(0)
        rest_pen.forward(43)
    turtle.tracer(True)
    
def bank():
    global player_info
    player_info['money'][turn] += 5
    money()
    turns()

'''
[Turn Function description]
This function allows the players to be swaped
in an designated order.
'''
def turns():
    global turn, roll
    money()
    if turn == 3:
        turn -= 3
    else:
        turn += 1
    roll = True
'''
[Countrys Function description]
Like its name it stamps the countrys flags on the board
so players can differentiate between the different countries.
'''
def countrys():
    global pen,board
    turtle.tracer(False)
    pen.setheading(180)
    pen.penup()
    pen.goto(360,-280)
    idx = 0
    for key in board:
        pen.shape(key)
        pen.forward(80)
        pen.stamp()
        if idx!=0 and idx%7==0:
            pen.right(90)
        idx+=1

    pen.setheading(180)
    pen.goto(240,-320)
    pen.pendown()
    for k in range(4):
        for i in range(7):
            for j in range(4):
                pen.forward(80)
                pen.right(90)
            pen.forward(80)
        pen.right(90)
        pen.forward(80)
    pen.penup()   
    turtle.tracer(True)
'''
[Character Function description]
It allows the players to move in a correct way of turning and going straight.
It also allows the players to travel, get stuck and etc on specific places.
'''    
def character(moves):
    global players,turn,player_info,country_orders,roll
    turtle.tracer(True)
    for i in range(moves):
        players[turn].forward(80)
        player_info['moves'][turn]+=1
        if player_info['moves'][turn]==28:
            player_info['moves'][turn]=0
            player_info['money'][turn]+=20
            #Fmoney()
        if player_info['moves'][turn]%7==0:
            players[turn].right(90)

    turtle.tracer(False)
    print(turn,country_orders[player_info['moves'][turn]])
    city_name = country_orders[player_info['moves'][turn]]
    for i in range(4):
        if city_name in player_info['own'][i]:
            player_info['money'][turn] -= board[city_name]['price']//2
            player_info['money'][i] += board[city_name]['price']//2
            #money()
            turns()
            return None
    turtle.tracer(False)
    no_owner = [0,7,14,21,4,18,25]
    if player_info['moves'][turn] in no_owner:
        if player_info['moves'][turn] ==21:
            travel()
        elif player_info['moves'][turn]==7:
            island()
        elif player_info['moves'][turn]==14:
            bank()
        else:
            turns()
    else:
        card(country_orders[player_info['moves'][turn]])

    print('turn',turn)
'''
[Card Function description]
This function allows the players to see what country they have landed to and
gives them a question whether they want to buy the land or not.
'''      
def card(cities):
    global board, card_stat, card_turtle
    card_stat = True

    card_turtle.goto(-120,200)
    card_turtle.color('white')
    card_turtle.begin_fill()
    for i in range(2):
        card_turtle.forward(240)
        card_turtle.right(90)
        card_turtle.forward(400)
        card_turtle.right(90)
    card_turtle.end_fill()
    card_turtle.penup()
    card_turtle.goto(0,100)
    card_turtle.shape(cities)
    card_turtle.stamp()
    card_turtle.goto(0,50)
    card_turtle.color('black')
    card_turtle.hideturtle()
    card_turtle.write(cities,align='center',font=('arial',20,'bold'))
    card_turtle.goto(0,-20)
    card_turtle.write(f"buying fee: {board[cities]['price']}",align='center',font=('arial',15,'normal'))
    card_turtle.goto(0,-40)
    card_turtle.write(f"price when crossing: {(board[cities]['price'])/2}",align='center',font=('arial',15,'normal'))
    card_turtle.goto(-90,-60)
    card_turtle.setheading(0)
    card_turtle.begin_fill()
    for i in range(2):
        card_turtle.forward(80)
        card_turtle.right(90)
        card_turtle.forward(100)
        card_turtle.right(90)
    card_turtle.end_fill()
    card_turtle.goto(10,-60)
    card_turtle.begin_fill()
    for i in range(2):
        card_turtle.forward(80)
        card_turtle.right(90)
        card_turtle.forward(100)
        card_turtle.right(90)
    card_turtle.end_fill()
    card_turtle.color('white')
    card_turtle.goto(-50,-120)
    card_turtle.write('Buy',align='center',font=('arial',25,'bold'))
    card_turtle.goto(50,-120)
    card_turtle.write('Pass',align='center',font=('arial',25,'bold'))
'''
[Money Function description]
It shows the current money of a player each time they have bought, or
gained money so they know whether they are going to buy a land.
'''  
def money():
    global player_info, pen
    turtle.tracer(False)
    pen_m.clear()
    pen_m.penup()
    pen_m.color("black")
    pen_m.goto(-297.5,-360.5)
    pen_m.setheading(0)
    for i in range(4):
        pen_m.write(f"player{i+1} profit = {player_info['money'][i]}",align='center',font=('arial',15,'bold'))
        pen_m.forward(195)
    turtle.tracer(True)
'''
[Own Function description]
This function makes the player stamp on a land they have so they know who
will earn the money.
'''  
def own(city):
    global board, pen, turn, players, player_info
    player_info['own'][turn].append(city)
    players[turn].shape('circle')
    players[turn].stamp()
    players[turn].shape('turtle')

    


pen=turtle.Turtle()
turtle.setup(800,800)
board={'Start':{'image':'python/blue_marble/images/Start.png','price':20},
       'London':{'image':'python/blue_marble/images/Britain.png','price':28},
       'Paris':{'image':'python/blue_marble/images/France.png','price':25},
       'Rome':{'image':'python/blue_marble/images/Italy.png','price':27},
       'Lucky_Card_E':{'image':'python/blue_marble/images/Lucky_card.png','price':0},
       'Bern':{'image':'python/blue_marble/images/Switzerland.png','price':29},
       'Berlin':{'image':'python/blue_marble/images/Germany.png','price':31},
       'Island':{'image':'python/blue_marble/images/island.png','price':32},
       'Mogadishu':{'image':'python/blue_marble/images/Somalia.png','price':27},
       'Rabat':{'image':'python/blue_marble/images/Moroco.png','price':30},
       'Accra':{'image':'python/blue_marble/images/Ghana.png','price':28},
       'Concord':{'image':'python/blue_marble/images/Concord.jpg','price':35},
       'Antananarivo':{'image':'python/blue_marble/images/Madagascar.png','price':33},
       'Nairobi':{'image':'python/blue_marble/images/Kenya.png','price':20},
       'World_Bank':{'image':'python/blue_marble/images/World_Bank.jpg','price':10},
       'Washington_DC':{'image':'python/blue_marble/images/USA.png','price':45},
       'Brasilia':{'image':'python/blue_marble/images/Brazil.png','price':39},
       'Mexico_City':{'image':'python/blue_marble/images/Mexico.png','price':37},
       'Lucky_Card_NS':{'image':'python/blue_marble/images/Lucky_card.png','price':0},
       'Otawa':{'image':'python/blue_marble/images/Canada.png','price':42},
       'Buenos_Aires':{'image':'python/blue_marble/images/Argentina.png','price':45},
       'Rocket':{'image':'python/blue_marble/images/Rocket.png','price':20},
       'Beijing':{'image':'python/blue_marble/images/China.png','price':60},
       'Abudabi':{'image':'python/blue_marble/images/UAE.png','price':65},
       'Manila':{'image':'python/blue_marble/images/Philipines.png','price':50},
       'Lucky_Card_A':{'image':'python/blue_marble/images/Lucky_card.png','price':0},
       'Tokyo':{'image':'python/blue_marble/images/Japan.png','price':55},
       'Seoul' :{'image':'python/blue_marble/images/South_Korea.png','price':100}}


scr =turtle.Screen()
not_country=['Start','Island','World_Bank','Rocket']
roll = True
for key in board:
    image = Image.open(board[key]['image'])
    if key not in not_country:
        image = image.resize((60,40))
    else:
        image = image.resize((80,80))
    img_t = ImageTk.PhotoImage(image)
    scr.register_shape(key,turtle.Shape('image',img_t))
countrys()
card_turtle=turtle.Turtle()
card_turtle.hideturtle()
sell_turtle = turtle.Turtle()
players=[turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()]
colors=['red','yellow','green','blue']
pen_m=turtle.Turtle()
placement=[[260,-260],[300,-260],[260,-300],[300,-300]]
country_orders=['Start',
                'London',
                'Paris',
                'Rome',
                'Lucky_Card_E',
                'Bern',
                'Berlin',
                'Island',
                'Mogadishu',
                'Rabat',
                'Accra',
                'Concord',
                'Antananarivo',
                'Nairobi',
                'World_Bank',
                'Washington_DC',
                'Brasilia',
                'Mexico_City',
                'Lucky_Card_NS',
                'Otawa',
                'Buenos_Aires',
                'Rocket',
                'Beijing',
                'Abudabi',
                'Manila',
                'Lucky_Card_A',
                'Tokyo',
                'Seoul']
player_info={'moves':[0,0,0,0],'money':[70,150,150,150], 'own':[[],[],[],[]], 'island':[0,0,0,0]}
traveler_pen = turtle.Turtle()
traveler_pen.hideturtle()
rest_pen = turtle.Turtle()
rest_pen.hideturtle()
rest_pen.shape('circle')
rest_pen.shapesize(0.8)
game_stadium(0,0)
for i in range(4):
    players[i].penup()
    players[i].goto(placement[i])
    players[i].setheading(180)
    players[i].shape('turtle')
    players[i].shapesize(1.5)
    players[i].color(colors[i])
card_stat = False
turn=0
rest()
#print(scr.getshapes())
turtle.onscreenclick(dice)
turtle.mainloop()