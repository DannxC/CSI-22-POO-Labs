import turtle

# Definindo o número de quadrados
n = 5

# Definindo o lado do primeiro quadrado
init_size = 20

# Iniciando a tela
wn = turtle.Screen()
wn.bgcolor("#90EE90")

# Iniciando o turtle (Pen)
alex = turtle.Turtle()
alex.width(3)
alex.color("#FF69B4")
alex.speed(10)
alex.penup()
alex.goto(0 - 1 * init_size / 2, 0 - 1 * init_size / 2)
alex.pendown()

# Percorrendo na tela
for i in range(1, n + 1):
    # Desenhando o quadrado
    for j in range(4):
        alex.forward(i * init_size)
        alex.left(90)
    # Movendo o Pen para a posição do próximo quadrado
    alex.penup()
    alex.goto(0 - (i + 1) * init_size / 2, 0 - (i + 1) * init_size / 2)
    alex.pendown()
wn.mainloop()