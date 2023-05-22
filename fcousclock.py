import time
import turtle

def timer(t):
    """模拟专注时钟的函数"""
    for i in range(t):
        # 模拟专注时钟的操作
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        time.sleep(0.5)

turtle.speed(0)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
timer(60)
turtle.hideturtle()
turtle.done()
