import time
from turtle import Turtle
import json
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for both dev and PyInstaller bundles. """
    if hasattr(sys, '_MEIPASS'):
        # If running from a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # If running in normal Python environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

config_file_path = resource_path('config.json')

# Load configuration
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
SPEED = config["SNAKE_SPEED"]
COLOR = config["SNAKE_COLOR"]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color(COLOR)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[seg - 1].xcor()
            y_axis = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_axis, y_axis)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() != DOWN:

            self.head.setheading(UP)
            time.sleep(0.01)
    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)
            time.sleep(0.01)
    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)
            time.sleep(0.01)
    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)
            time.sleep(0.01)
