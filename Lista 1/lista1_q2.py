import turtle

# Função para desenhar um polígono qualquer
def draw_poly(t, n, sz):
    """
    t -> referencia da turtle
    n -> numero de lados
    sz -> tamanho dos lados
    """
    for i in range(n):
        alex.forward(sz)
        alex.left(360/n)

# Iniciando a tela
wn = turtle.Screen()
wn.bgcolor("#90EE90")

# Iniciando o turtle (Pen)
alex = turtle.Turtle()
alex.width(3)
alex.color("#FF69B4")
alex.speed(10)

# Desenhar Polígono
draw_poly(alex, 8, 50)

wn.mainloop()