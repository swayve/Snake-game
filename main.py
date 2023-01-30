from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


#Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(5)


#making of the snake segments(blocks)
bound = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(bound.up, "Up")
screen.onkey(bound.left, "Left")
screen.onkey(bound.right, "Right")
screen.onkey(bound.down, "Down")
scoreboard
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    bound.move()

    #detect collision with snake and food
    if bound.head.distance(food) < 15:
        food.refresh()
        bound.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if bound.head.xcor() > 280 or bound.head.xcor() < -280 or bound.head.ycor() > 280 or bound.head.ycor() > 280 or bound.head.ycor() < -280:
       game_on = False
       scoreboard.game_over()
    
    #detect collision with on body(tail)
    for segment in bound.segments[1:]:
        if bound.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()



game_on = True



