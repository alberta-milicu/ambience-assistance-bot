import csv
import PySimpleGUI as sg
from csv import DictReader


##header = ['Name', 'Temperature', 'Blood_Pressure', 'Illness', 'Time']
##with open("csv_file", 'a', encoding='UTF8', newline='') as csvfile:
## writer = csv.writer(csvfile)
## writer.writerow(header)

class Disease:
    def __init__(self, name, ambient):
        self.name = name
        self.ambient = ambient

    def getambient(self):
        return self.ambient


class Ambient:
    def __init__(self, temperature, humidity, air_quality):
        self.temperature = temperature
        self.humidity = humidity
        self.air_quality = air_quality

    def toString(self):
        print(
            "temperature : " + self.temperature + " humidity :" + self.humidity + " air_quality : " + self.air_quality)


class Person:
    def __init__(self,name,temperature,blood_pressure,illnesses):
        self.name = name
        self.temperature = temperature
        self.blood_pressure = blood_pressure
        self.illnesses = illnesses

    def __gettemperature__(self):
        return self.temperature


def analyze(a, b):
    if (int(a.temperature) > 24) and (int(b.temperature) > 30):
        print(" " + a.name + " should not leave their home ")
    else:
        print(" " + a.name + " is able to leave their home")


def store(person,time):
    csv_counter = 0
    with open("csv_file") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            csv_counter += 1

    if csv_counter < 50:

        with open("csv_file", 'a', encoding='UTF8', newline='') as csvfile:
            writer = csv.writer(csvfile)

            print("Time : ")

            data = [person.name, person.temperature, person.blood_pressure, person.illnesses, time]
            writer.writerow(data)
            # csvfile.writelines(person.name + person.temperature + person.blood_pressure + person.illnesses + a)
            csvfile.close()
    else: sg.Popup("The database is full!",
                     keep_on_top=True)


def reports(time):
    #print("Type of time : ")
    #a = input()
    thislist = list()
    i = 0
    with open("csv_file") as csvfile:
        csv_dict_reader = DictReader(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        for row in csv_dict_reader:
            if time in row['Time']:
                thislist.insert(i,row)
                i += i


    return (thislist)


if __name__ == "__main__":
    #c1 = Ambient(31, 10, 15)
    # p2 = Person()
    # analyze(p2, c1)
    # store(p2)
    #reports()

    sg.theme('DarkTeal6')

    layout = [
        [sg.Text('Hello! I am BOT-Man, your virtual assistant. How may I help you today?', key='text1', visible=True)],
        [sg.Text('Please fill in the form:', key='text2', visible=False)],
        [sg.Button('Register', key='button1', visible=True)],
        [sg.Button('Analyze', key='analyze', visible=True)],

        [sg.Radio('Daily:', 'RADIO1', default=False, key="daily_check", visible=True)],
        [sg.Radio('Weekly:', 'RADIO1', default=False, key="weekly_check", visible=True)],
        [sg.Radio('Monthly:', 'RADIO1', default=False, key="monthly_check", visible=True)],
        [sg.Radio('Yearly:', 'RADIO1', default=False, key="yearly_check", visible=True)],

        [sg.Text('Name', key='name_tag', size=(15, 1), visible=False), sg.InputText(key='name', visible=False)],
        [sg.Text('Body Temperature', key='temperature_tag', size=(15, 1), visible=False),
         sg.InputText(key='temperature', visible=False)],
        [sg.Text('Blood pressure', key='bp_tag', size=(15, 1), visible=False), sg.InputText(key='bp', visible=False)],

        [sg.Text('Disease', key='disease_tag', size=(15, 1), visible=False)],
        [sg.Combo(
            ['Heart Disease', 'Diabetes', 'Arthritis', 'Osteoporosis', 'AIDS', 'Asthma', 'COPD', 'ADHD', 'Dementia',
             'Depression'], key='disease', visible=False)],

        [sg.Text('Data type', key='dt_tag', size=(15, 1), visible=False)],
        [sg.Combo(['Daily', 'Weekly', 'Monthly', 'Yearly'], key='dt', visible=False)],

        [sg.Button('Submit', key='submit', visible=False)]
    ]

    # Create the window
    window = sg.Window("BOT-Man", layout, size=(800, 500))

    # Create an event loop
    while True:
        event, values = window.read()

        if event == 'button1':
            window['text2'].Update(visible=True)
            window['text1'].Update(visible=False)
            window['button1'].Update(visible=False)
            window['analyze'].Update(visible=False)
            window['daily_check'].Update(visible=False)
            window['weekly_check'].Update(visible=False)
            window['monthly_check'].Update(visible=False)
            window['yearly_check'].Update(visible=False)

            window['name_tag'].Update(visible=True)
            window['name'].Update(visible=True)

            window['temperature_tag'].Update(visible=True)
            window['temperature'].Update(visible=True)

            window['bp_tag'].Update(visible=True)
            window['bp'].Update(visible=True)

            window['disease_tag'].Update(visible=True)
            window['disease'].Update(visible=True)

            window['dt_tag'].Update(visible=True)
            window['dt'].Update(visible=True)

            window['submit'].Update(visible=True)

        elif event == 'submit':
            combo = values['disease']
            combo2 = values['dt']
            p1 = Person(layout[8][1].get(),layout[9][1].get(),layout[10][1].get(),combo)
            #print(p1.name + p1.temperature + p1.blood_pressure  + p1.illnesses)
            store(p1,combo2)
            sg.Popup('Recommended ambient: \nRoom temperature: 23 deg C \nHumidity: 5% \nAir quality >= 90%',
                     keep_on_top=True)
            window['text2'].Update(visible=False)
            window['text1'].Update(visible=True)
            window['button1'].Update(visible=True)
            window['analyze'].Update(visible=True)
            window['daily_check'].Update(visible=True)
            window['weekly_check'].Update(visible=True)
            window['monthly_check'].Update(visible=True)
            window['yearly_check'].Update(visible=True)

            window['name_tag'].Update(visible=False)
            window['name'].Update(visible=False)

            window['temperature_tag'].Update(visible=False)
            window['temperature'].Update(visible=False)

            window['bp_tag'].Update(visible=False)
            window['bp'].Update(visible=False)

            window['disease_tag'].Update(visible=False)
            window['disease'].Update(visible=False)

            window['dt_tag'].Update(visible=False)
            window['dt'].Update(visible=False)

            window['submit'].Update(visible=False)

        # elif event == 'analyze':
        elif values['daily_check']:
            a = reports("Daily")
            sg.Popup(a,
                     keep_on_top=True)
        elif values['weekly_check']:
            a = reports("Weekly")
            sg.Popup(a,
                     keep_on_top=True)
        elif values['monthly_check']:
            a = reports("Monthly")
            sg.Popup(a,
                     keep_on_top=True)
        elif values['yearly_check']:
            a = reports("Yearly")
            sg.Popup(a,
                     keep_on_top=True)

        elif event == sg.WIN_CLOSED:
            break




    window.close()
