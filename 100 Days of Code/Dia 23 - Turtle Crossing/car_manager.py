from turtle import Turtle
import random

COLORS = ["#A80000", "#FB6400", "#FFC400", "#62BA27", "#3342C4", "#9362C4",
          "#194BF0", "#E62B3C", "#FC9328", "#FED140", "#48358B", "#37A514"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    Gerencia os carros do jogo.
    """
    def __init__(self):
        """
        Construtor da classe.

        Cria uma lista para armazenar os carros e uma variável para armazenar a velocidade.
        """
        self.cars = list()
        self.car_speed = STARTING_MOVE_DISTANCE

    def gen_cars(self):
        """
        Gera novos carros e armazena na lista se um número gerado aleatóriamente for igual a 6.
        """
        if random.randint(1, 6) == 6:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=320, y=random.randint(-240, 240))

            self.cars.append(new_car)

    def move_cars(self):
        """
        Move os carros para frente.
        """
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_difficulty(self):
        """
        Aumenta a dificuldade em 10
        """
        self.car_speed += MOVE_INCREMENT
