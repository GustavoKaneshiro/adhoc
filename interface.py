import PySimpleGUI as sg

 #criar janelas e estilos
def initial_window():
    sg.theme('Reddit')
    list1 = ['User Info', 'Average Info Between Placements']
    layout = [
        [sg.Text('Choose an option', size=(20,0)), sg.Combo(values = list(list1), key='option', size=(15,1))],
        [sg.Button('Ok')]
    ]
    return sg.Window('Start', layout = layout, finalize = True)

def user_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text('User Name', size=(15,0)), sg.Input(size=(15,0), key='username')],
        [sg.Text('Choose an option', size=(20,0))], 
        [
            sg.Checkbox('Placement Info', key='1'), 
            sg.Checkbox('Average Placement Info', key='2'), 
            sg.Checkbox('Gold Info', key='3')
        ],
        [
            sg.Checkbox('Average Gold Info', key='4'), 
            sg.Checkbox('Level Info', key='5'), 
            sg.Checkbox('Time Eliminated Info', key='6')
        ],
        [
            sg.Checkbox('Average Time Eliminated Info', key='7'), 
            sg.Checkbox('Players Eliminated Info', key='8'), 
            sg.Checkbox('Total Damage to Players Info', key='9')
        ],
        [
            sg.Checkbox('Average Total Damage to Players Info', key='10'), 
            sg.Checkbox('Last Round Info', key='11'), 
            sg.Checkbox('Average Last Round Info', key='12')
        ],
        [sg.Button('Ok'), sg.Button('Back')]
    ]
    return sg.Window('User', layout = layout, finalize = True)

def average_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Choose an option', size=(20,0))],
        [
            sg.Checkbox('Average Gold Info', key='1'), 
            sg.Checkbox('Average Level Info', key='2'), 
            sg.Checkbox('Average Time Eliminated Info', key='3')
        ],
        [
            sg.Checkbox('Average Players Eliminated Info', key='4'), 
            sg.Checkbox('Average Total Damage to Players Info', key='5'), 
            sg.Checkbox('Average Last Round Info', key='6')
        ],
        [sg.Button('Ok'), sg.Button('Back')]
    ]
    return sg.Window('Average', layout = layout, finalize = True)

#criar janelas iniciais
window1, window2, window3 = initial_window(), None, None

#oop de eventos
while True:
    window, event, values = sg.read_all_windows()
    
    #janela fechada
    if window == window1 and event == sg.WIN_CLOSED:
        break

    if window == window2 and event == sg.WIN_CLOSED:
        break

    if window == window3 and event == sg.WIN_CLOSED:
        break
    
    #proxima janela
    if window == window1 and event == 'Ok' and values['option'] == 'User':
        window2 = user_window()
        window1.hide()

    if window == window1 and event == 'Ok' and values['option'] == 'Average':
        window3 = average_window()
        window1.hide()
    
    #janela anterior
    if window == window2 and event == 'Back':
        window2.hide()
        window1.un_hide()

    if window == window3 and event == 'Back':
        window3.hide()
        window1.un_hide()
    #eventos
    if window == window2 and event == 'Ok':
        username = values['username']

        if values['1'] == True:
            sg.popup(f'{username} user 1')
        if values['2'] == True:
            sg.popup(f'{username} user 2')
        if values['3'] == True:
            sg.popup(f'{username} user 3')
        if values['4'] == True:
            sg.popup(f'{username} user 4')
        if values['5'] == True:
            sg.popup(f'{username} user 5')
        if values['6'] == True:
            sg.popup(f'{username} user 6')
        if values['7'] == True:
            sg.popup(f'{username} user 7')
        if values['8'] == True:
            sg.popup(f'{username} user 8')
        if values['9'] == True:
            sg.popup(f'{username} user 9')
        if values['10'] == True:
            sg.popup(f'{username} user 10')
        if values['11'] == True:
            sg.popup(f'{username} user 11')
        if values['12'] == True:
            sg.popup(f'{username} user 12')

    if window == window3 and event == 'Ok':

        if values['1'] == True:
            sg.popup('average 6')
        if values['2'] == True:
            sg.popup('average 6')
        if values['3'] == True:
            sg.popup('average 6')
        if values['4'] == True:
            sg.popup('average 6')
        if values['5'] == True:
            sg.popup('average 6')
        if values['6'] == True:
            sg.popup('average 6')
      
