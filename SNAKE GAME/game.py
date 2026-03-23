
from food import Food
from snake import Snake
from turtle import Screen,Turtle
from scoreboards import Scoreboard
turtle=Turtle()
scoreboards=Scoreboard()
import time
food=Food()
screen=Screen()
snake=Snake()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(height=600,width=600)
screen.title("My Snake Game")
screen.listen()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detect collision with food
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        scoreboards.refresh_score()
    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboards.reset()
        snake.reset()

    if snake.head.distance(snake.tail)<1:
        scoreboards.reset()
        snake.reset()

   #for i in snake.segments[1:]:
   #    if snake.head.distance(i)<10:
   #        is_game_on=False
   #        scoreboards.reset()












screen.exitonclick()





















screen.exitonclick()