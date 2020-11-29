import PySimpleGUI as sg

class Viewer():

    def inicio(self):
        return self.menu()

    def menu(self):
        sg.theme('Reddit')
        list1 = ['User Info', 'Average Info Between Placements']
        layout = [
            [sg.Text('Choose an option', size=(20, 0)), sg.Combo(values=list(list1), key='option', size=(28, 1))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Menu', layout)
        while 1:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                print('Quit')
                return 3
            if event == 'Ok':
                if values['option'] == "User Info":
                    window.close()
                    return 1
                if values['option'] == "Average Info Between Placements":
                    window.close()
                    return 2
                else:
                    window.close()
                    return 3

    def userMenu(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('User Name', size=(15, 0)), sg.Input(size=(15, 0), key='username')],
            [sg.Text('Choose an option', size=(20, 0))],
            [
                sg.Checkbox('Placement Info', key='1'),
                sg.Checkbox('Average Placement Info', key='2'),
                sg.Checkbox('Gold Info', key='3')
            ],
            [
                sg.Checkbox('Average Gold Info', key='4'),
                sg.Checkbox('Level Info', key='5'),
                sg.Checkbox('Average Level Info', key='6'),
            ],
            [
                sg.Checkbox('Time Eliminated Info', key='7'),
                sg.Checkbox('Average Time Eliminated Info', key='8'),
                sg.Checkbox('PLayers Eliminated Info', key='9')
            ],
            [
                sg.Checkbox('Average Players Eliminated Info', key='10'),
                sg.Checkbox('Total Damage to Players Info', key='11'),
                sg.Checkbox('Average Total Damage to Players Info', key='12'),
            ],
            [
                sg.Checkbox('Last Round Info', key='13'),
                sg.Checkbox('Average Last Round Info', key='14')
            ],
            [sg.Button('Ok'), sg.Button('Back')]
        ]
        window = sg.Window('User Menu', layout)

        while 1:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                print('Quit')
                return 16
            if event == 'Ok':
                selected = [values['username']]
                print(selected)
                for item in values:
                    if values[item]:
                        if item != 'username':
                            selected.append(item)
                window.close()
                return selected

    def avgMenu(self):

        lugar_up = ['1', '2', '3', '4', '5', '6', '7', '8']
        lugar_lower = ['1', '2', '3', '4', '5', '6', '7', '8']

        sg.theme('Reddit')
        layout = [
            [sg.Text('Select Range', size=(20, 0))],
            [sg.Text('Choose an option - Max placement', size=(20, 0)), sg.Combo(values=list(lugar_up), key='upper',
                                                                                 size=(15, 1), enable_events=True)],
            [sg.Text('Choose an option - Min placement', size=(20, 0)), sg.Combo(values=list(lugar_lower), key='lower',
                                                                                 size=(15, 1), enable_events=True)],
            [sg.Text('Choose an option', size=(20, 0))],
            [
                sg.Checkbox('Average Gold Info', key='9'),
                sg.Checkbox('Average Level Info', key='10'),
                sg.Checkbox('Average Time Eliminated Info', key='11')
            ],
            [
                sg.Checkbox('Average Players Eliminated Info', key='12'),
                sg.Checkbox('Average Total Damage to Players Info', key='13'),
                sg.Checkbox('Average Last Round Info', key='14')
            ],
            [sg.Button('Ok'), sg.Button('Back')]
        ]
        window = sg.Window('Average Menu', layout)
        while 1:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                return 8
            if event == "Ok":
                if values['upper'] and values['lower']:
                    selected = []
                    limits = [int(values['upper']), int(values['lower'])]
                    selected.append(limits)
                    for item in values:
                        if values[item] and item != "upper" and item != "lower":
                            selected.append(item)
                    window.close()
                    return selected
            if event == "upper":
                new_lower = []
                for i in range(int(values['upper']), 9):
                    new_lower.append(str(i))

                window.find_element('lower').Update(values=new_lower)
            if event == "lower":
                new_up = []
                for i in range(1, int(values['lower'])+1):
                    new_up.append(str(i))

                window.find_element('upper').Update(values=new_up)
