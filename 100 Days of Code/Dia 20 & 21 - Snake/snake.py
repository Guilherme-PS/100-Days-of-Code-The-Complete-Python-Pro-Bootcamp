from turtle import Turtle

SNAKE_COLOR = "#F4C2C2"

STARTING_POSITIONS = [(0, 0), (-21, 0), (-42, 0)]
DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Inicializa a Snake e cria os segments iniciais.
    """
    def __init__(self):
        self.segments = list()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adiciona um novo segmento à Snake na posição especificada.
        :param position: Posição em que vai ser adiconado um segmento.
        """
        new_segment = Turtle(shape="square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)

    def extend(self):
        """
        Adiciona um novo segmento à Snake na última posição ocupada pelo último segmento.
        """
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """
        Remove a Snake da tela e retorna a posição inicial.
        """
        for segment in self.segments:
            segment.goto(x=1000, y=1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """
        Move a Snake para a próxima posição.
        """
        for num in range(len(self.segments) - 1, 0, -1):
            position_x = self.segments[num - 1].xcor()
            position_y = self.segments[num - 1].ycor()

            self.segments[num].goto(x=position_x, y=position_y)

        self.head.forward(DISTANCE)

    def up(self):
        """
        Move a Snake para cima, se ela não estiver se movendo para baixo.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Move a Snake para baixo, se ela não estiver se movendo para cima.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Move a Snake para a esquerda, se ela não estiver se movendo para a direita.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Move a Snake para a direita, se ela não estiver se movendo para a esquerda.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)