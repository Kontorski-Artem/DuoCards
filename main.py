from cards import *

lst_of_nums = [chr(x) for x in range(48, 58)]
instr = []

# Формирование инструкции для программы
def on_key(event):
    if event.name in lst_of_nums:
        instr.append(event.name)

    if event.name == "backspace" and len(instr):
        instr.pop()

on_press(on_key)

# Главный цикл main
while True:
    # Пауза
    if is_pressed('p'):
        wait('p')

    # Запуск основного файла
    if len(instr) == 4:
        main(instr)
        instr = []

    sleep(0.01)
