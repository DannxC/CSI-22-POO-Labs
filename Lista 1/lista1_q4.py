import turtle

# Função para desenhar um polígono qualquer
def draw_spiral(t, n, ang):
    """
    t -> referencia da turtle
    n -> numero de lados desenhados
    ang -> angulo entre cada lado
    """
    for i in range(n + 1):
        alex.forward(2 * i)
        alex.left(ang)

# Iniciando a tela
wn = turtle.Screen()
wn.bgcolor("#90EE90")

# Iniciando o turtle (Pen)
alex = turtle.Turtle()
alex.width(1)
alex.color("#4877C7")
alex.speed(10)

# Desenhar a espiral com 90º
alex.penup()
alex.goto(-200, 0)
alex.pendown()
draw_spiral(alex, 99, -90)

# Desenhar a espiral com 89º
alex.penup()
alex.goto(200, 0)
alex.pendown()
draw_spiral(alex, 99, -89)

wn.mainloop()