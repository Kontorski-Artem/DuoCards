from pyautogui import click
from time import sleep
from keyboard import *
import threading

loop = True

# Выход из программы
def end():
    wait('q')

    global loop
    loop = False

# Программа
def cards(instr):
    count = 0
    time = .35
    global loop

    all_place = ['0', '1', '2', '3', '4']

    # Число, которого нет в instr q
    num = int(list(set(all_place) - set(instr))[0])


    # Выполняется нажатие на кнопку из левой колонки и на кнопку из правой колонки
    def click_in_w(p, t):
        num = int(p)

        click(800, 760 - 80*instr.index(p))
        click(1075, 435 + 80*num)
        sleep(t)

    while loop:
        if count == 1:
            instr = [instr[1], instr[0], instr[2], instr[3]]

        # Проверяем каждое число из инструкции на совпадение со всеми возможными числами
        # При совпадении (оно будет всегда) выполняется функция click_in_w
        for place in instr:
            for n in all_place:
                if place == n:
                    click_in_w(place, time)
                    break

        count += 1

    click(800, 435)
    click(1075, 435 + 80 * num)
    loop = True

    return

def main(instr):
    # создаем потоки для каждой функции
    thread1 = threading.Thread(target=end)
    thread2 = threading.Thread(target=cards, args=[instr])

    # запускаем потоки
    thread2.start()
    thread1.start()

    # ждем завершения обоих потоков
    thread2.join()
    thread1.join()


if __name__ == "__main__":
    main(["1", "4", "2", "3"])
