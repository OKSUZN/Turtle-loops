import turtle as turtle

turtle.shape("turtle")
turtle.color("orange")

aantal_hoeken = int (input("geef hoeken "))

for n in range (aantal_hoeken):
    turtle.forward(90)
    turtle.right(360/aantal_hoeken)
turtle.done()