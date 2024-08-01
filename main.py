from turtle import Screen
from food import Food
from scorecard import Score
import time
from snake import Snake
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Road to Success !")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorecard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scorecard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorecard.game_over()







screen.exitonclick()