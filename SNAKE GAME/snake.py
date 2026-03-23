positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance=20
up=90
down=270
left=180
right=0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.tail=self.segments[-1]
        self.head = self.segments[0]
    def create_snake(self):
        for pos in positions:
            self.add_segment(pos)
    def add_segment(self,pos):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(move_distance)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
    #def back(self):
    #    self.temp = self.head.heading(up)
    #    self.head.heading(up) = self.head.heading(down)
    #    self.head.heading(down)=self.temp
#

