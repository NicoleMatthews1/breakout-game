from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
BLOCK_LENGTHS = [1, 1.5, 2, 2.5, 3, 3.5, 4, 1, 1.5, 2, 2.5, 3, 3.5, 4, 1, 1.5, 2, 2.5, 3, 3.5, 4, 1]

#BLOCK_LENGTHS = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 3.5]


class BlockManager(Turtle):

    def __init__(self):
        self.blocks = []


    def add_rows(self):
        y_position = 280
        for color in COLORS:
            random.shuffle(BLOCK_LENGTHS)
            x_position = -595
            i = 0
            for block in BLOCK_LENGTHS:
                new_block = Turtle()
                new_block.shape("square")
                new_block.shapesize(stretch_len=block)
                new_block.penup()
                new_block.color(color)
                x_position += block*20/2 + 5
                new_block.goto(x_position, y_position)
                x_position += block * 20 /2
                i +=1
                self.blocks.append(new_block)
            y_position -= 25
