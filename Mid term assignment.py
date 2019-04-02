from microbit import*

a = 0
b = 0
c = 0
bitpattern = []
while True:
    if c < 31:
        if button_a.was_pressed():
            display.set_pixel(a, b, 9)
        if button_b.was_pressed():
            if display.get_pixel(4,4) == 9:
                display.clear()
                a = 0
                b = 0
            elif a < 4 :
                a = a + 1
                c = c + 1
            elif a <= 4 and b <= 4:
                a = 0
                b = b + 1
                c = c + 1
    else:
        display.clear()

