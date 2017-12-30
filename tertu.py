import turtle


def draw_things():
    avery = turtle.Pen()
    avery.forward(50)
    avery.right(90)
    avery.forward(20)

    kate = turtle.Pen()
    kate.left(90)
    kate.forward(100)

    jacob = turtle.Pen()
    jacob.left(180)
    jacob.forward(80)

    input("Press a key in the console...")


if __name__ == '__main__':
    draw_things()
