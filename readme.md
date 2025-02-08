# Monopoly(Kr . Version)
This programs is the recreation of the game called Blue marble as known as Monopoly for english speakers. I made this program as monopoly is one of my favorite board game yet has a big disadvantage of being to big to bring around. To solve this I wanted to make this on computer as it takes up less space and weight to bring around.

## Periods of Development
> July 6 2024 - Now

## Development Environment
> Python

## Core Features
### 말이 움직이는 방법
![image](https://github.com/user-attachments/assets/35565fc2-44f6-49d8-91ed-b4e05c24e4a7)
When the roll button is clicked, it opperates the dice code which sends its value(in this case a 5)to the character function, the character function then adds the current value of the dice and the previous value from player info. When the total amount exeeds the multiples of 7 it makes a turn allowing it to move in a square direction.




<div style="display: flex; justify-content: space-around;">

  <img src='https://github.com/user-attachments/assets/85846204-48d7-4aa1-9ca7-7c242b81e4e6' width='500px' height='150px'/>
  <img src='https://github.com/user-attachments/assets/0ec66918-b20b-4bbf-8aa6-08b92f5621fe' width='500px' height='150px'/>
</div>
Whenever the character makes a full turn: the player info, which contains the information about total movement sends the information to character, then the character detects that the total movement is greater than or equal to 28 and adds 20 money to the playerinfo's money section and subtracts 28 from their total movement.


### 자유여행
![image](https://github.com/user-attachments/assets/7a69c97e-1e5e-4ddb-bb57-99a52dc1dd10)
When the players total movement is 21 characters calls the travel_select function which then pops up this image asking if the player wants to travel to a selected country.
![image](https://github.com/user-attachments/assets/08a817f7-18b5-44f1-997e-3270a6bf344b)
When the player does select yes, then the travel_select function calls the travel function which draws a white square indicating to click on a land that the player wants to goto. While that happens the travel_select function also calls the fider function which has the information about which coordinates the countries, calls the character function and tells where the player has to goto.
### 무인도
<div style='display:flex; justify-content:center'>
  <img src ='https://github.com/user-attachments/assets/47bbef27-9478-4ec1-bb29-77754be736fd' width='500px' height='500px'/>
  <div style='display:flex; justify-content:center flex-direction:column'>
    <img src ='https://github.com/user-attachments/assets/4b0f891e-dc84-47c7-875f-2abed021d5fa' width='500px' height='200px'/>
    <img src ='https://github.com/user-attachments/assets/bb56f763-59d5-436f-9ed5-6bc3197ce9fb' width='500px' height='200px'/>
  </div>
</div>
This photo shows what happens when the player arives to the "Islands" land. When the player's total movement becomes 7 the characters detects that and calls the islands function. The islands function then changes the "playerinfo[islands]" into 3 making indicating that the players stuck there for 3 rounds. To make this visual, the islands function calls the rest function which visually shows the "playerinfo[islands]" visually with the players colour to show which player is stuck there. Also as the turn goes by, each rotation back to teh player in the (CONTINUE)
### 은행
![image](https://github.com/user-attachments/assets/dde67a87-d954-4d6a-b9c2-722565b39cb7)

### 카드
Every time a player lands on a city, they get a a card to pop up on their screen asking whether they would like to buy this land. The player can receive information sabout its cost and its earns every time another player steps on their land.
![image](https://github.com/user-attachments/assets/fecb2a3b-184b-4dd4-8470-a675f967db6a)
