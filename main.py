from logic import guess_number
import PySimpleGUI as sg

def get_range():
    sg.theme('LightBrown13')

    layout = [
        [sg.Text("Виберіть діапазон чисел для гри:", font=('Helvetica', 14))],
        [sg.Text("Від:", size=(5, 1), font=('Helvetica', 14)), sg.Input(key='-START-', size=(10, 1), font=('Helvetica', 14))],
        [sg.Text("До:", size=(5, 1), font=('Helvetica', 14)), sg.Input(key='-END-', size=(10, 1), font=('Helvetica', 14))],
        [sg.Button('Почати гру', font=('Helvetica', 14))],
    ]

    window = sg.Window('Вибір діапазону чисел', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Почати гру':
            try:
                start = int(values['-START-'])
                end = int(values['-END-'])
                guess_number(start, end)
            except ValueError:
                sg.popup("Будь ласка, введіть коректний діапазон чисел.", title="Помилка")

    window.close()

if __name__ == "__main__":
    get_range()
