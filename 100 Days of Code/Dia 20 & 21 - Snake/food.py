from turtle import Turtle
import random

class Food(Turtle):
    """
    Inicializa a comida com suas caracteristicas visuais e define sua posição.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#800000")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Renova a posição da comida em uma nova posição aleatória.
        :return:
        """
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))