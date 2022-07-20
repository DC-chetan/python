from turtle import Turtle
segment=[]
starting_position=[(0,0),(-20, 0),(-40, 0)]
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range (len(self.segments)-1, 0, 1):
            new_x = self.segments[seg_num - 1].xcor()
            new_x = self.segments[seg_num - 1].xcor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        self.head.segments[0].setheading(Up)
    def down(self):
        self.head.segments[0].setheading(Down)

    def left(self):
        self.head.segments[0].setheading(Left)
    def Right(self):
        self.head.segments[0].setheading(Right)



