import PySimpleGUI as sg
import random

def guess_number(start, end):
    secret_number = random.randint(start, end)
    attempts = 0

    sg.theme('LightBrown13')

    layout = [
        [sg.Text(f"Вгадайте число від {start} до {end}:", font=('Helvetica', 14))],
        [sg.Input(key='-INPUT-', size=(10, 1), font=('Helvetica', 14)), sg.Button('Відгадати', font=('Helvetica', 14))],
        [sg.Text("", size=(30, 1), key='-OUTPUT-', font=('Helvetica', 14))],
    ]

    window = sg.Window(f'Гра "Відгадай число від {start} до {end}"', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Відгадати':
            try:
                user_input = int(values['-INPUT-'])
                attempts += 1

                if user_input == secret_number:
                    window['-OUTPUT-'].update(f"Ви вгадали! Загадане число було {secret_number}. Кількість спроб: {attempts}", text_color='green')
                    sg.popup("Вітаємо! Ви вгадали число!", title="Виграш!")
                    break
                elif user_input < secret_number:
                    window['-OUTPUT-'].update("Число більше.", text_color='green')
                else:
                    window['-OUTPUT-'].update("Число менше.", text_color='red')
            except ValueError:
                window['-OUTPUT-'].update(f"Будь ласка, введіть число від {start} до {end}.", text_color='red')

    window.close()
